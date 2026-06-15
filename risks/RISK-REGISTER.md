# NimbusLedger Threat-Informed Risk Register

**Company:** NimbusLedger (fictional fintech SaaS)
**Last updated:** 2026-06-04
**Total risks:** 10
**Tactics covered:** Initial Access, Execution, Persistence, Privilege Escalation, Lateral Movement, Collection, Exfiltration

| ID    | Title                                        | Tactic               | Impact   | Likelihood | Inherent | Coverage | Residual | Owner         | Status     |
|-------|----------------------------------------------|----------------------|----------|------------|----------|----------|----------|---------------|------------|
| R-001 | Phishing — credential theft                  | Initial Access       | High     | High       | 16       | 62.5%    | 6        | CISO          | Monitoring |
| R-002 | Exploit public-facing application            | Initial Access       | Critical | Medium     | 15       | 75%      | 4        | Eng Lead      | Monitoring |
| R-003 | Credential stuffing via valid accounts       | Initial Access       | High     | High       | 16       | 75%      | 4        | CISO          | Monitoring |
| R-004 | External remote service compromise           | Initial Access       | High     | Medium     | 12       | 83.3%    | 2        | Eng Lead      | Monitoring |
| R-005 | Third-party vendor trusted relationship      | Initial Access       | High     | Medium     | 12       | 50%      | 6        | CISO          | Monitoring |
| R-006 | Malicious script execution on endpoint       | Execution            | High     | Medium     | 12       | 50%      | 6        | Eng Lead      | Open       |
| R-007 | Persistent backdoor via scheduled task       | Persistence          | High     | Medium     | 12       | 50%      | 6        | Eng Lead      | Open       |
| R-008 | Privilege escalation via AWS IAM misconfiguration | Privilege Escalation | Critical | Medium  | 15       | 70%      | 5        | CISO          | Monitoring |
| R-009 | Lateral movement via service account tokens  | Lateral Movement     | Critical | Medium     | 15       | 80%      | 3        | Eng Lead      | Monitoring |
| R-010 | Customer PII exfiltration via S3 bucket      | Collection/Exfil     | Critical | Medium     | 15       | 80%      | 3        | CISO          | Monitoring |
