# Threat-Informed Risk Register (TIRR)

Most risk registers describe risks in business terms - "unauthorized access," 
"data breach," "insider threat." They rarely connect those risks to how 
attackers actually operate, or to which specific controls reduce them.

This project closes that gap.

TIRR is a structured risk register for a fictional fintech SaaS company 
(NimbusLedger) that links each enterprise risk to the real adversary 
technique behind it (MITRE ATT&CK) and the specific controls that mitigate 
it (NIST 800-53), then scores how well-covered each risk actually is.

---

## Data model
Each risk entry answers four questions:
1. **What could go wrong?** - a specific, grounded scenario for NimbusLedger
2. **How would an attacker do it?** - mapped to MITRE ATT&CK technique IDs
3. **What defends against it?** - specific NIST 800-53 controls, rated yes / partial / no
4. **How covered are we?** - a quantitative coverage score and residual risk score

**Scoring logic:**
- `coverage_score` = (yes × 1 + partial × 0.5 + no × 0) ÷ total controls
- `inherent_risk_score` = impact_value × likelihood_value (each 1–5, max 25)
- `residual_risk_score` = inherent × (1 − coverage_score)

Coverage scores are computed automatically from YAML entries.
Run: `pip install pyyaml && python scripts/score_risks.py`

---

## Risk register

| ID    | Title                                        | Tactic                  | Impact   | Likelihood | Inherent | Coverage | Residual | Status     |
|-------|----------------------------------------------|-------------------------|----------|------------|----------|----------|----------|------------|
| R-001 | Phishing - credential theft                  | Initial Access          | High     | High       | 16       | 62.5%    | 6        | Monitoring |
| R-002 | Exploit public-facing application            | Initial Access          | Critical | Medium     | 15       | 75%      | 4        | Monitoring |
| R-003 | Credential stuffing via valid accounts       | Initial Access          | High     | High       | 16       | 75%      | 4        | Monitoring |
| R-004 | External remote service compromise           | Initial Access          | High     | Medium     | 12       | 83.3%    | 2        | Monitoring |
| R-005 | Third-party vendor trusted relationship      | Initial Access          | High     | Medium     | 12       | 50%      | 6        | Monitoring |
| R-006 | Malicious script execution on endpoint       | Execution               | High     | Medium     | 12       | 50%      | 6        | Open       |
| R-007 | Persistent backdoor via scheduled task       | Persistence             | High     | Medium     | 12       | 50%      | 6        | Open       |
| R-008 | Privilege escalation via AWS IAM misconfiguration | Privilege Escalation | Critical | Medium  | 15       | 70%      | 5        | Monitoring |
| R-009 | Lateral movement via service account tokens  | Lateral Movement        | Critical | Medium     | 15       | 80%      | 3        | Monitoring |
| R-010 | Customer PII exfiltration via S3 bucket      | Collection / Exfil      | Critical | Medium     | 15       | 80%      | 3        | Monitoring |

---

## Sample risk walkthrough - R-001

**Scenario:** Attackers send phishing emails to NimbusLedger employees 
targeting Okta SSO credentials. A successful compromise gives the attacker 
authenticated access to the AWS console and customer financial data.

**ATT&CK mapping:**
- T1566 - Phishing (Initial Access, TA0001)
- T1566.001 - Spearphishing Attachment

**Controls mapped:**

| Control | Name                          | Implemented |
|---------|-------------------------------|-------------|
| AT-2    | Security Awareness Training   | Yes         |
| IA-2(1) | MFA for Privileged Accounts   | Yes         |
| SI-3    | Malicious Code Protection     | Partial     |
| IA-5(1) | Phishing-Resistant Auth       | No          |

**Scores:**
- Inherent risk: 4 × 4 = **16 / 25**
- Coverage: (1 + 1 + 0.5 + 0) / 4 = **62.5%**
- Residual risk: 16 × (1 − 0.625) = **6 / 25**

**Recommendation:** Implement IA-5(1) - phishing-resistant authenticators 
(FIDO2 / hardware keys). This single control would raise coverage to 87.5% 
and reduce residual risk from 6 to 2.

---

## Tactics covered

| Tactic                | MITRE ID | Risk IDs        |
|-----------------------|----------|-----------------|
| Initial Access        | TA0001   | R-001 to R-005  |
| Execution             | TA0002   | R-006           |
| Persistence           | TA0003   | R-007           |
| Privilege Escalation  | TA0004   | R-008           |
| Lateral Movement      | TA0008   | R-009           |
| Collection            | TA0009   | R-010           |
| Exfiltration          | TA0010   | R-010           |

---

## Repo structure

threat-informed-risk-register/
├── risks/
│   ├── R-001.yaml through R-010.yaml   - risk entries
│   └── RISK-REGISTER.md                - consolidated table
├── controls/                           - NIST 800-53 reference
├── mappings/                           - ATT&CK ↔ 800-53 crosswalk
├── docs/
│   ├── company-profile.md              - NimbusLedger fictional company
│   ├── data-model.md                   - schema documentation
│   └── glossary.md                     - plain-English reference
└── scripts/
├── score_risks.py                  - coverage scoring engine
└── results.json                    - latest scoring output
---

## Fictional company

**NimbusLedger** - a B2B fintech SaaS company (80 employees, Wilmington DE) 
providing cloud-based accounting software to ~500 SMB clients. AWS-hosted 
(us-east-1), Okta SSO, Splunk Cloud SIEM, SOC 2 Type II in progress.

Full profile: [docs/company-profile.md](docs/company-profile.md)

---

## Frameworks referenced

| Framework       | Role in this project                        | Link |
|-----------------|---------------------------------------------|------|
| MITRE ATT&CK    | Adversary technique mapping                 | [attack.mitre.org](https://attack.mitre.org) |
| NIST SP 800-53  | Security control catalog                    | [csrc.nist.gov](https://csrc.nist.gov/projects/risk-management/sp800-53-controls) |
| NIST CSF 2.0    | Risk management context (Identify, Protect, Detect, Respond, Recover) | [nist.gov/cyberframework](https://www.nist.gov/cyberframework) |

---

## Author

**Om Satam** - MS Cybersecurity, University of Delaware  
[linkedin.com/in/om-satam](https://linkedin.com/in/om-satam) · [github.com/GRCguy14](https://github.com/GRCguy14)
