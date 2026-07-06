# Chapter 1 — LLM Fundamentals

**VP Interview Prep — AI & AI Infrastructure Concepts**
Companion reference for `vp_engineering_interview_prep.md`. Every concept below is explained twice — in plain English (the CEO-facing version) and in technical terms (the principal-engineer-facing version) — and grounded in real projects: **UniClaw** (open-source vehicle-agent platform), **IAH** (CruxOCM's Industrial Automation Hub), **TestBOT** (the Robot Framework test-authoring agent), and CruxOCM/Insulet infrastructure work.

**Interview one-liner for this whole chapter:**
> "Fine-tuning changes how a model behaves; RAG changes what it knows; prompting is how you get 80% of the value before spending on either."

---

## 1.1 The generation loop

A decoder-only model (GPT, Claude, Gemini) generates text one fragment at a time, in five repeating steps.

```
1. Prompt text  →  2. Tokenization  →  3. Embedding  →  4. Transformer stack  →  5. Next-token prediction ↻
```

### 1 · Prompt text

- **Plain English:** The model has no memory between calls. Every "conversation" is an illusion your application maintains — each turn, your app re-sends the system prompt, the entire chat history, the tool definitions, and the new message as one block of text. If something isn't in this request, the model does not know it, no matter how many times you've told it before.
- **Technical terms:** The input sequence is the serialization of system prompt + message history + tool schemas + prior tool results. Statelessness pushes all conversation-state management to the application layer. Prompt ordering discipline — stable content first, volatile content last — is the structural prerequisite for **prompt caching** (Chapter 2's biggest cost lever).
- **UniClaw example:** When a user texts "unlock my car" on Telegram, UniClaw assembles the full prompt from scratch: the agent's system instructions ("confirm before irreversible actions"), the tool catalog (lock, unlock, climate, locate), the recent turns from that Telegram chat, and the new message. If the same user messages tomorrow from a different channel, the model has no idea who they are unless UniClaw's session layer re-supplies that context — one reason supporting 12 channels is an application-state problem, not a model problem.
- **IAH example:** The pipebot troubleshooting agent on GCP ADK splits into a stable prefix (agent instructions, tool definitions for telemetry queries and log search) and a volatile tail (the incident description plus tool results that accumulate each loop iteration). Because ADK re-sends the whole conversation every turn, context grows turn over turn — why **agent cost grows roughly quadratically with conversation length**, and why tool-result hygiene (Chapter 4) exists.

### 2 · Tokenization

- **Plain English:** The model reads word-fragments, not words. Common words are one fragment; rare words, names, and technical strings shatter into several. Everything you're billed for, everything the context limit counts, and everything that determines speed is denominated in these fragments.
- **Technical terms:** Byte-pair encoding (BPE) builds a fixed vocabulary (32K–200K subword entries) by merging frequent character pairs; English averages ~0.75 words per token. Code, JSON, logs, and non-English text tokenize less efficiently. Tokenizers differ across providers, so cross-vendor cost comparisons must be measured in tokens-per-task, never words or lines.
- **UniClaw example:** "Unlock the Honda" is ~4–5 tokens, but the vehicle-status JSON a provider adapter returns (nested fields, VINs, timestamps, coordinates) can be several hundred — and per point 1, that JSON gets re-billed as input on every subsequent turn until it ages out.
- **TestBOT example:** Robot Framework's keyword-driven, whitespace-separated syntax is token-inefficient — long keyword names and tabular spacing mean cost-per-line-of-test runs higher than prose suggests. Forecast generation cost by tokenizing real sample outputs, not by estimating from line counts.

### 3 · Embedding

- **Plain English:** Each fragment is converted into a point in a vast "meaning space" where similar concepts sit near each other — that geometric neighborhood is why the model handles phrasings it has never seen, rather than doing keyword matching.
- **Technical terms:** Each token ID indexes a row in a learned embedding matrix (hidden dimension in the thousands), combined with positional information so order matters. Keep two artifacts distinct: the LLM's **internal** embeddings (never exposed to you) vs. **standalone embedding models** used to build retrieval indexes — related technology, different products, different price points.
- **UniClaw example:** "unlock my car," "open her up," and "let me in the Civic" all land in the same neighborhood, so the agent routes all three to the same unlock tool without a coded synonym list. Contrast with UniClaw's no-LLM menu mode, where users must pick exact predefined options — meaning-space vs. string matching.
- **IAH example:** Adding semantic retrieval over runbooks and past incident reports for the troubleshooting agent means chunking and indexing those documents with a dedicated embedding model in a vector store — the LLM's internal embeddings are never touched to do this. This distinction is a common interview trap.

### 4 · Transformer stack

- **Plain English:** Dozens of identical layers, each letting every fragment "look at" everything before it and refine its meaning — this repeated cross-referencing is the intelligence you're renting. Bigger stacks are smarter, slower, and more expensive.
- **Technical terms:** N layers of attention + feed-forward blocks (see 1.2 below). Capability tracks parameter count across tiers (2–8B, 30–70B, 100B+); per-token compute is proportional to parameters; attention cost grows with context length; the K/V vectors produced in every layer get cached during generation.
- **UniClaw example:** The three AI modes are a stack-size dial in one config flag — Claude API mode (frontier-scale stack, best multi-step tool-use reasoning), local Gemma via Ollama (2–8B stack, fine for command routing, weaker at multi-step planning), no-LLM mode (zero stack, fully deterministic). A working ninety-second answer to "how do you think about build vs. buy."
- **IAH example:** Connecting "pressure dropping at pump 7" to a valve-state change buried earlier in the context is the stack doing long-range cross-referencing — the capability behind IAH's "94% reduction in manual ops" claim.

### 5 · Next-token prediction

- **Plain English:** The model produces a probability list over every possible next fragment, picks one, appends it, and repeats. Two consequences: output is sequential (long answers take time; streaming hides this), and "hallucination" is a statistically plausible pick that happens to be wrong — the model predicts text, it doesn't know facts.
- **Technical terms:** A softmax over the vocabulary, sampled with temperature/top-p; structured-output modes constrain decoding to valid JSON or a schema; tool use means the model emits a schema-conformant tool-call block that your **runtime** — not the model — executes. Decode is one forward pass per token, defining time-per-output-token (TPOT).
- **UniClaw example:** The model could fluently generate "Done — your car is unlocked" with nothing having happened. UniClaw never treats generated prose as ground truth: state changes happen only through tool calls against the FastAPI vehicle layer, and unlock specifically sits behind a human confirmation gate. Design principle: **the model proposes, the system disposes.**
- **TestBOT example:** Low temperature + schema-constrained output so Robot Framework syntax parses — and generated tests are executed before acceptance. Generation is never trusted un-run; this is the same discipline that generalizes into agent evals (Chapter 7).

---

## 1.2 Attention — what happens inside the stack

### Inside one transformer layer

```
Input vectors
   → Multi-head self-attention   (tokens exchange information)
   → Add & normalize             (residual connection)
   → Feed-forward network        (each token processed alone)
   → Add & normalize             (residual again)
   → Output vectors → next layer
```

- **Multi-head self-attention:** the only place tokens talk to each other. Several heads run in parallel, each tracking a different kind of relationship (grammar, entity reference, long-range topic). The K and V vectors computed here are exactly what gets stored in the **KV cache** during generation.
- **Add & normalize:** a residual (skip) connection plus layer normalization — each sublayer computes a small edit to a running "residual stream" rather than a full rewrite. This is what makes 100-layer networks trainable.
- **Feed-forward network (FFN):** each token is processed independently — no cross-token mixing. Holds roughly two-thirds of the model's parameters; widely understood as where much of the model's stored knowledge lives. Decode speed is dominated by streaming these weights through the GPU (memory-bandwidth bound).

**Infrastructure example:** attention's cost scales with sequence length (the cross-token part — long context hits here, and its K/V outputs fill GPU memory as cache); the FFN's cost is per-token and parameter-heavy (why serving is bandwidth-bound during decode). Being able to name which box a symptom belongs to (e.g., "we quantized to fit the GPU" → FFN; "long contexts blew up our memory" → attention) is what separates a leader who understands the stack from one reciting vendor slides.

### Attention weights across the three steps

**1 · Query token** — *Plain English:* as each word is processed, it effectively asks "who back there matters to me right now?" — how pronouns find referents and instructions bind to objects.
*Technical:* the token's current vector is projected into a query vector Q, compared against key vectors K of every prior position; a causal mask restricts attention to backwards-only in decoder-only models.
*UniClaw:* "actually, lock it instead" — "it" must reach back to "the Honda" from three turns ago; that coreference across re-sent chat history is attention doing its job, and it only works because the history is in context (Chapter 1.1, point 1).
*IAH:* an operator asks "why did it trip?" mid-session, referring to an alarm surfaced many tool-results earlier. If context management pruned that result to save tokens, attention cannot recover it — retention policy determines what attention can even see.

**2 · Attention fan** — *Plain English:* focus is distributed as weights — most near zero, a few strong — and focus quality degrades when the relevant fact is buried mid-context ("lost in the middle"). More context is not monotonically better.
*Technical:* softmax(QKᵀ/√d)·V per head; prefill computes all pairwise interactions (compute grows ~quadratically with context length); decode attends across the entire cached K/V (linear per token). Both mean long-context requests are slower and pricier.
*IAH:* dumping 80K tokens of raw telemetry means the needle is technically in context but effectively missed — the argument for pre-filtering/summarizing telemetry before it enters the prompt rather than dumping and praying.
*UniClaw:* running Gemma locally through Ollama on a long chat shows rising per-token latency and memory — decode attending over an ever-longer KV cache; `num_ctx` is a hard bound on this growth.

**3 · Layer stack** — *Plain English:* the looking-and-blending repeats layer after layer; many heads per layer track different relationship types.
*Technical:* KV cache per sequence ≈ 2 × layers × heads × head-dim × context-length × bytes — linear in context, per concurrent request, competing with batch size for the same GPU memory.
*Infrastructure:* a 7–8B model at FP16 needs ~14–16 GB for weights alone; a few concurrent 16–32K-token conversations add gigabytes more cache — the GPU that "fits the model" on paper doesn't fit the workload (the Azure VM exploration story).
*IAH:* also why "give the agent everything" isn't a strategy even when self-hosting on-prem — existing customer infrastructure has finite VRAM.

---

## 1.3 Training pipeline

```
1. Pretraining  →  [ Post-training: 2. Supervised fine-tuning → 3. RLHF / RLAIF ]
```

### 1 · Pretraining

- **Plain English:** the model reads a colossal slice of human text, endlessly guessing the next fragment, absorbing language, knowledge, code, and reasoning as a side effect. You never run this step; only frontier labs do.
- **Technical terms:** self-supervised next-token prediction over trillions of tokens, months on thousands of GPUs, tens–hundreds of millions of dollars; capability follows scaling laws. Output is a **base model** — knowledgeable but not helpful (completes text, doesn't follow instructions).
- **UniClaw example:** the agent knows a Civic is a Honda and can parse "warm up the car before my 8am" — none of which you taught it. Pretrained knowledge rented for fractions of a cent per request; why "build our own model" is almost never the right AI-strategy answer.
- **IAH example:** base models arrive knowing generic control-systems vocabulary (SCADA, PID loops, setpoints) but nothing about pipebot's behavior or a customer's asset configuration. That gap is filled by context (prompting/retrieval), not more training.

### 2 · Supervised fine-tuning (SFT)

- **Plain English:** show the model thousands of examples of desired behavior — input in, ideal output out — until it imitates the pattern. Teaches format and procedure; does not reliably teach new facts.
- **Technical terms:** supervised gradient descent on instruction–response pairs; LoRA/PEFT methods make it cheap (hours on one GPU). Risks: catastrophic forgetting, style overfitting. Data quality dominates quantity.
- **Crux example:** fine-tuning a small model on 5,000 resolved incidents ("symptoms → diagnosis → remediation") teaches your triage structure beautifully — and still won't know site 12 replaced its valve controller last month. Structure from fine-tuning, facts from context.
- **TestBOT example:** a corpus of human-accepted Robot Framework tests is ready-made SFT data for house conventions (naming, setup/teardown, tagging), while *what* to test still arrives per-prompt — the correctly-shaped fine-tuning proposal.

### 3 · RLHF / RLAIF

- **Plain English:** candidate answers are ranked by humans (or an AI judge applying written principles), and the model is nudged toward preferred answers. Tone, helpfulness, and refusals come from here — you inherit a vendor's judgment along with their model.
- **Technical terms:** a reward model trained on preference pairs, optimized via PPO, or trained directly via DPO. RLAIF substitutes AI feedback guided by explicit principles, scaling past human-rating throughput.
- **UniClaw example:** Claude asking "which vehicle did you mean?" instead of guessing is inherited post-training. Operational flip side: a provider model update can shift agent behavior with zero code change — pin model versions, run regression evals on upgrades, the same discipline as never blind-upgrading a Kubernetes control plane.
- **IAH example:** in OT environments, vendor post-training is necessary but never sufficient safety. IAH's own governance language — operator control, operating within physical constraints — is correct architecture: post-training shapes tendencies; the platform enforces invariants through deterministic guardrails and approval gates.

---

## 1.4 The adaptation ladder — prompting vs. RAG vs. fine-tuning

```
1. Prompting  →  2. RAG  →  3. Fine-tuning
(increasing cost, effort, and iteration time; burden of proof is on moving up)
```

### 1 · Prompting

- **Plain English:** change what you ask and how — instructions, examples, structure. Minutes to iterate, zero infrastructure, and where 80% of production value comes from.
- **Technical terms:** few-shot exemplars, structured output schemas, and tool schemas (agents choose tools by reading names/descriptions, so tool naming *is* prompt engineering). Treat prompts like code: versioned, reviewed, regression-tested against an eval suite.
- **UniClaw example:** "always confirm before unlock" is a system-prompt rule + tool-design decision (the confirmation gate) — no model surgery. Edit text, redeploy in minutes.
- **IAH example:** the troubleshooting agent's diagnostic methodology (alarms → trends → correlate with recent commands) lives as instructions, tuned against a suite of historical incidents.

### 2 · RAG

- **Plain English:** instead of hoping the model knows your facts, look up relevant documents at question time and hand them over. Changes what the model *knows* without touching the model.
- **Technical terms:** chunk → embed → index (vector store) → retrieve top-k → (rerank) → generate with citations. Enforce ACL filtering at query time; run freshness pipelines. Full pipeline in Chapter 5.
- **IAH example:** runbooks get revised, P&IDs change, incident history accumulates, and every customer site differs — retrieval means today's answer cites today's runbook revision, and per-customer retrieval scopes naturally respect tenant boundaries.
- **UniClaw example:** "how do I pair my key fob?" across 27 brands' owner manuals is textbook RAG — retrieve the relevant page rather than fine-tuning Gemma on a PDF.

### 3 · Fine-tuning

- **Plain English:** retrain the model's habits so it reliably produces your format/style/dialect without being told every time. Justified for consistency and unit cost at volume — never for injecting facts (unreliable, instantly stale).
- **Technical terms:** LoRA-based SFT on a small open-weight model; win condition = narrow task + stable format + high sustained volume; entry ticket = an eval suite comparing against the prompted frontier baseline.
- **TestBOT example:** at thousands of generated tests/month, a fine-tuned 7–8B model trained on your accepted-test corpus could match frontier output for this one narrow task at a fraction of the cost, and run self-hosted if a customer demands it.
- **UniClaw example:** the config flag is the whole ladder in one artifact — Claude mode (rung 1 on a frontier model), Gemma mode (where rung-3 thinking lands), menu mode (sometimes the right amount of LLM is zero).

---

## 1.5 Model landscape

| Tier | Examples | Character | Your evidence |
|---|---|---|---|
| **Frontier APIs (100B+)** | Anthropic, OpenAI, Google | Best quality, zero ops, elastic, per-token pricing; data leaves your tenant | UniClaw Claude mode; Gemini Enterprise rollout (the hard part was tenancy/governance, not the model) |
| **Open-weight mid-size (30–70B)** | Llama, Qwen, DeepSeek, Mistral | Serious self-hosting; worth it above ~40–60% GPU utilization or under data-residency mandates | Azure VM exploration; IAH's promise to run inside existing customer infrastructure, on-prem or cloud |
| **Open-weight small (2–8B)** | Gemma, small Llama/Qwen, distilled models | Runs on one GPU or a laptop; covers a surprising share of narrow production workloads | UniClaw's local-Gemma-via-Ollama mode; industrial edge deployment with no internet dependency |

**The synthesis (say this in every AI-strategy round):** the question is never "which model is best," it's "which tier does this workload deserve" — and **hybrid** (frontier API for hard reasoning, small self-hosted models for high-volume narrow tasks, connected by a routing layer) is almost always the real answer. Routing by difficulty is often a 60–90% cost reduction — the single biggest lever in Chapter 2.

---

## Quick-reference one-liners

- **Adaptation ladder:** "Fine-tuning changes how a model behaves; RAG changes what it knows; prompting is how you get 80% of the value before spending on either."
- **Generation loop:** "It's an extremely well-read autocomplete that predicts one word-fragment at a time — everything we pay for and wait on comes from how much text goes in and how many fragments come out."
- **Transformer layer:** "Each layer is a group discussion followed by quiet individual thinking — the discussion is attention, the thinking is where the knowledge lives, and we stack that a hundred times."
- **Model landscape:** "The question is never which model is best, it's which tier does this workload deserve — hybrid is almost always the real answer."

---

## Sources for this chapter

Grounded in `vp_engineering_interview_prep.md` (Part 1.1–1.9), the CruxOCM IAH product page (`cruxocm.com/industrial-automation-hub`), and prep-session drill-downs. UniClaw and TestBOT architecture details reflect the descriptions captured in the prep doc (provider registry, scoped JWTs, three AI modes, 4,400+ tests, Robot Framework test-authoring agent) — connect a GitHub source to ground future chapters at the code level.
