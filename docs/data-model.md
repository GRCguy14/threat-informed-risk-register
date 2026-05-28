# TIRR Data Model

## Core relationship
Risk → ATT&CK Technique(s) → NIST 800-53 Control(s) → Coverage Score

Each enterprise risk is linked to the adversary technique(s) that could
realize it, then to the control(s) that mitigate it. The ratio of
implemented controls to required controls produces a coverage score.

## Entities

### Risk
- risk_id (R-001)
- title, description
- business_impact: low | medium | high | critical
- likelihood: low | medium | high
- inherent_risk_score (impact × likelihood, 1–25)
- residual_risk_score (after controls)
- owner, status, last_reviewed

### ATT&CK Technique (linked to a Risk)
- id (T1566), name, tactic (TA0001 Initial Access)

### NIST 800-53 Control (linked to a Risk)
- id (IA-2(1)), name
- implemented: yes | partial | no

### Coverage Score (derived)
- coverage_score = implemented_controls / total_mapped_controls
- "partial" counts as 0.5

## Scoring logic
- inherent_risk_score = impact_value × likelihood_value (each 1–5)
- coverage_score drives residual: higher coverage → lower residual
- residual_risk_score = inherent × (1 − coverage_score), rounded

## Schema format
Risk entries stored as YAML, one file per risk in /risks.
See README for a full example entry.
