# Tailored Head-of-Automation resume — <Company>

Copy of this folder per company. Steps:

1. Copy `../../Resume_HeadOfAutomation_Generic.md` here as `Resume_HeadOfAutomation_<Company>.md`.
2. Tailor summary + bullets to the JD in `../../../../companies/<company>/role-and-jd.md`.
3. Generate the PDF: `docker compose run --rm pdf resumes/head-of-automation/companies/<company>/Resume_HeadOfAutomation_<Company>.md` → outputs `Resume_Ishan_Shah.pdf` here.
4. Log the version + status in `../../../../tracking/interview_tracker_master.csv`.

Delete this README once the folder has a real resume, or keep it as a checklist.
