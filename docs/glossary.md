# Glossary

A plain-English reference for the frameworks, codes, and terms used in
this Threat-Informed Risk Register.

---

## Frameworks

### MITRE ATT&CK
A free, public knowledge base of real-world adversary tactics and
techniques. Maintained by the MITRE Corporation (a nonprofit) and used
across the security industry as a common language for describing how
attackers operate. Browse at: https://attack.mitre.org

- **Tactic** - the attacker's *goal* at a given stage
  (e.g., Initial Access = "get in the door").
- **Technique** - the *specific method* used to achieve a tactic
  (e.g., Phishing is a technique used to achieve Initial Access).
- **Technique ID** - every technique has a unique code starting with
  `T` (e.g., T1566). Sub-techniques add a decimal (e.g., T1566.001).

### NIST SP 800-53
A free, public catalog of security and privacy controls published by
the U.S. National Institute of Standards and Technology. Used by
federal agencies and widely adopted in private-sector GRC programs.
Each control has an ID where the letters identify the family
(category) and the number identifies the specific control. Enhancements
appear in parentheses, e.g., IA-2(1).
Browse at: https://csrc.nist.gov/projects/risk-management/sp800-53-controls

### NIST CSF
NIST Cybersecurity Framework - a higher-level framework organized into
five functions: Identify, Protect, Detect, Respond, Recover. Not used
directly in this register's data model but referenced for context.

---

## Risk scoring (used in this project)

| Value | Impact / Likelihood |
|-------|---------------------|
| 1     | Very low            |
| 2     | Low                 |
| 3     | Medium              |
| 4     | High                |
| 5     | Critical / Very high|

- **inherent_risk_score** = impact_value × likelihood_value (1–25)
- **coverage_score** = sum of implemented controls ÷ count of controls
  - implemented `yes` = 1
  - implemented `partial` = 0.5
  - implemented `no` = 0
- **residual_risk_score** = inherent_risk_score × (1 - coverage_score),
  rounded to nearest whole number

---

## MITRE ATT&CK techniques used in this project

| ID         | Name                                  | Tactic              |
|------------|---------------------------------------|---------------------|
| T1566      | Phishing                              | Initial Access      |
| T1566.001  | Spearphishing Attachment              | Initial Access      |
| T1190      | Exploit Public-Facing Application     | Initial Access      |
| T1078      | Valid Accounts                        | Initial Access      |
| T1133      | External Remote Services              | Initial Access      |
| T1199      | Trusted Relationship                  | Initial Access      |

---

## NIST 800-53 control families used in this project

The first letters of every control ID identify its family.

| Family | Name                                  | What it covers                                                     |
|--------|---------------------------------------|--------------------------------------------------------------------|
| AC     | Access Control                        | Who is allowed to access what, and how access is managed           |
| AT     | Awareness and Training                | Security education for staff                                       |
| AU     | Audit and Accountability              | Logging, monitoring, and tracking system activity                  |
| CA     | Assessment, Authorization, Monitoring | Checking and approving systems and external connections            |
| IA     | Identification and Authentication     | Verifying identity - logins, MFA, credentials                      |
| RA     | Risk Assessment                       | Identifying and analyzing risks (vuln scanning lives here too)     |
| SA     | System and Services Acquisition       | Managing vendors, suppliers, and third-party services              |
| SC     | System and Communications Protection  | Protecting networks and data in transit (firewalls, encryption)    |
| SI     | System and Information Integrity      | Patching, anti-malware, input validation, integrity checks         |

---

## NIST 800-53 controls used in this project

| ID        | Name                                          | Plain meaning                                                                 |
|-----------|-----------------------------------------------|-------------------------------------------------------------------------------|
| AC-2      | Account Management                            | Creating, managing, and removing user accounts properly                       |
| AC-6      | Least Privilege                               | Users get only the minimum access needed for their job                        |
| AC-17     | Remote Access                                 | Rules for connecting from outside the network (VPN, remote admin)             |
| AT-2      | Literacy Training and Awareness               | General security awareness training for all staff                             |
| AU-12     | Audit Record Generation                       | Systems generate logs of significant events                                   |
| CA-3      | Information Exchange                          | Formal agreements when systems share data with external parties               |
| IA-2      | Identification and Authentication (Users)     | Verifying users are who they claim to be                                      |
| IA-2(1)   | MFA for Privileged Accounts                   | Enhancement on IA-2 — multi-factor auth required for admin accounts          |
| IA-5(1)   | Authenticator Management — Password-based     | Phishing-resistant authenticators (e.g., hardware keys, FIDO2)                |
| RA-3      | Risk Assessment                               | Conducting formal risk assessments on systems and operations                  |
| RA-5      | Vulnerability Monitoring and Scanning         | Regularly scanning systems for known vulnerabilities                          |
| SA-9      | External System Services                      | Managing security risk from third-party SaaS, vendors, integrations           |
| SC-7      | Boundary Protection                           | Firewalls and controls at the network edge                                    |
| SC-8      | Transmission Confidentiality and Integrity    | Encrypting data while it moves across networks (TLS, etc.)                    |
| SI-2      | Flaw Remediation                              | Patching vulnerabilities and fixing software flaws in a timely manner         |
| SI-3      | Malicious Code Protection                     | Anti-malware / anti-virus on endpoints and servers                            |
| SI-10     | Information Input Validation                  | Validating user input to prevent injection attacks                            |

---

## Other terms used

- **GRC** - Governance, Risk, and Compliance. The discipline of ensuring
  an organization manages risk and meets its obligations.
- **ISMS** - Information Security Management System. The set of policies,
  procedures, and controls that govern how an organization protects
  information.
- **Inherent risk** - the level of risk before any controls are applied.
- **Residual risk** - the level of risk remaining after controls reduce
  the inherent risk.
- **Crown jewels** - the most valuable assets an organization needs
  to protect.
- **Threat-informed** - making risk and control decisions based on
  knowledge of how real adversaries actually operate, rather than
  abstract risk categories.
