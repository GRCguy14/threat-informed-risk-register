"""
score_risks.py
Reads all risk YAML files in /risks and outputs a coverage
summary to /scripts/results.json
"""

import os
import json
import yaml

RISKS_DIR = os.path.join(os.path.dirname(__file__), '..', 'risks')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'results.json')

def score_controls(controls):
    if not controls:
        return 0.0
    scores = {'yes': 1.0, 'partial': 0.5, 'no': 0.0}
    total = sum(scores.get(c.get('implemented', 'no'), 0.0) for c in controls)
    return round(total / len(controls), 3)

def load_risks():
    risks = []
    for fname in sorted(os.listdir(RISKS_DIR)):
        if fname.endswith('.yaml') and fname.startswith('R-'):
            fpath = os.path.join(RISKS_DIR, fname)
            with open(fpath, 'r') as f:
                risk = yaml.safe_load(f)
                risks.append(risk)
    return risks

def summarize(risks):
    results = []
    for r in risks:
        controls = r.get('mitigating_controls', [])
        coverage = score_controls(controls)
        inherent = r.get('inherent_risk_score', 0)
        residual = round(inherent * (1 - coverage), 1)
        results.append({
            'risk_id': r.get('risk_id'),
            'title': r.get('title'),
            'business_impact': r.get('business_impact'),
            'likelihood': r.get('likelihood'),
            'inherent_risk_score': inherent,
            'coverage_score': coverage,
            'residual_risk_score': residual,
            'control_count': len(controls),
            'controls_implemented': sum(
                1 for c in controls if c.get('implemented') == 'yes'
            ),
            'controls_partial': sum(
                1 for c in controls if c.get('implemented') == 'partial'
            ),
            'controls_missing': sum(
                1 for c in controls if c.get('implemented') == 'no'
            ),
        })
    return results

def main():
    risks = load_risks()
    results = summarize(risks)

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Scored {len(results)} risks. Output: {OUTPUT_FILE}\n")
    print(f"{'ID':<8} {'Coverage':>10} {'Inherent':>10} {'Residual':>10}  Title")
    print("-" * 75)
    for r in results:
        print(
            f"{r['risk_id']:<8}"
            f"{r['coverage_score']:>10.1%}"
            f"{r['inherent_risk_score']:>10}"
            f"{r['residual_risk_score']:>10}  "
            f"{r['title'][:45]}"
        )

if __name__ == '__main__':
    main()
