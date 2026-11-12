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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

Responders handling simultaneous incidents need to see which records share a signal and region so they can investigate related reports together.

## Project walkthrough

```mermaid
flowchart LR
    A["Incident CSV"]
    B["Group incident IDs by signal and region"]
    C{"Group contains multiple incidents?"}
    D["Emit incident IDs and count"]
    E["Omit singleton group"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
