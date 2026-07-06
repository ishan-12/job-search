#!/usr/bin/env bash
# One-time setup: point git at the versioned hooks in .githooks/.
# Run once per clone:  bash tools/setup-hooks.sh
set -euo pipefail

cd "$(dirname "$0")/.."
git config core.hooksPath .githooks
chmod +x .githooks/* 2>/dev/null || true

echo "✓ Git hooks enabled (core.hooksPath = .githooks)"
echo "  - pre-commit : gitleaks scan + sensitive-file & large-file guards +"
echo "                 PDF-generation tests (when the generator or a resume changes)"
echo "  - commit-msg : <=80 chars/line + no AI attribution"
