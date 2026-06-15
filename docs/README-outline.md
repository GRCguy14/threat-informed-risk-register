# README Outline (draft — ship Friday)

## Hook (2-3 sentences)
Why threat-informed risk registers are better than traditional ones.
The gap this project closes.

## What this is
One-paragraph project description.
Link to company profile (docs/company-profile.md).

## Data model
Risk → ATT&CK Technique → NIST 800-53 Control → Coverage Score
Small ASCII diagram or table.

## Risk register summary
Paste the RISK-REGISTER.md table here.

## Sample risk walkthrough
Walk through R-001 (Phishing) end to end.
Explain each field, the scoring math, the recommendation.

## Coverage scoring
How the Python script works.
How to run it: `pip install pyyaml && python scripts/score_risks.py`

## Tactics covered
Table: Tactic | Technique IDs | Risk IDs
Initial Access, Execution, Persistence,
Privilege Escalation, Lateral Movement,
Collection, Exfiltration

## Frameworks referenced
MITRE ATT&CK (link), NIST 800-53 (link), NIST CSF (link)

## Author
Om Satam — MS Cybersecurity, University of Delaware
GitHub: GRCguy14
