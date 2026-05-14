# AML/CFT/CPF Policy Framework Builder for Indian VDA SPs

An open-source structured framework for drafting AML/CFT/CPF policies for Indian Virtual Digital Asset Service Providers (VDA SPs), anchored to the **FIU-IND AML & CFT Guidelines dated January 8, 2026**, PMLA 2002, and PML Rules 2005.

## What it does

Answer 19 firm-profile questions. Get back a customised 60-80 page starting draft policy paragraph-anchored to current Indian regulation.

The output is calibrated to your firm profile: size, customer base, geography, custody model, tech stack, governance structure, compliance staffing, banking status, STR history, regulatory engagement history.

## What it is NOT

- Not legal advice
- Not a finished policy
- Not a substitute for qualified Indian legal counsel
- Not a substitute for operational implementation

Every output must be customised, validated, and routed through legal review before adoption.

## How it works

18 modular JSON files, each anchored to specific paragraphs of the 2026 FIU-IND Guidelines. A Python composer reads the modules, evaluates 14 conditional blocks across 7 modules against user input, and assembles the final Markdown policy.

## Local installation

```bash
git clone https://github.com/JapneetOnchain/aml-policy-builder.git
cd aml-policy-builder
pip install -r requirements.txt
python -m streamlit run src/app.py
```

## Regulatory sources

- FIU-IND AML & CFT Guidelines (January 8, 2026): https://fiuindia.gov.in/pdfs/downloads/VDA08012026.pdf
- PMLA 2002 and PML Rules 2005: https://fiuindia.gov.in/files/AML_Legislation/notification.html

## Author

Built by Japneet Singh - financial crime compliance professional with five years of AML experience across EY, KPMG, American Express, and NAB.

## Contributions

Open source. Contributions, corrections, and peer review welcomed. Open an issue or PR.

See `LIMITATIONS.md` for honest disclosure of what the tool does and does not capture.
