# Company Profile — "NimbusLedger" (fictional)

## Snapshot
- **Industry:** Fintech SaaS (B2B accounting software)
- **Employees:** 80
- **HQ:** Wilmington, DE (remote-first)
- **Customers:** ~500 SMB clients across US

## Tech stack
- AWS-hosted (us-east-1 primary, us-west-2 DR)
- Application: React frontend, Node.js backend, PostgreSQL (RDS)
- Auth: Okta SSO + AWS IAM Identity Center
- Logging: CloudTrail + CloudWatch → SIEM (Splunk Cloud)
- CI/CD: GitHub Actions → AWS

## Crown jewels
- Customer financial records (PII + financial data)
- Production AWS infrastructure (RDS, S3 buckets)
- Source code repositories
- Customer Okta credentials

## Compliance posture
- SOC 2 Type II (in progress)
- PCI DSS scope (limited — payments via Stripe)
- Customers expect GDPR + CCPA compliance

## Threat model assumptions
- External attackers (financially motivated) are primary concern
- Phishing + credential theft against employees is high-likelihood
- Public-facing SaaS app is a high-value target
- Third-party SaaS vendors create supply-chain exposure
