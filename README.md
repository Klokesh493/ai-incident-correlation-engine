# AI Incident Correlation Engine

Groups AI platform incidents by shared signals so SREs can spot common causes across models, jobs, and services.

Focus: incident response, AI/ML platform reliability, correlation analysis, SRE.

Portfolio framing: Apple-scale client-style platform project using synthetic data only.

## Run

```bash
python3 incident_correlation.py sample_incidents.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
