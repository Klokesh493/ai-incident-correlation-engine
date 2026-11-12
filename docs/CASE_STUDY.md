# Ai Incident Correlation Engine walkthrough

## Business problem

Responders handling simultaneous incidents need to see which records share a signal and region so they can investigate related reports together.

## Reproduce the workflow

Run `python3 incident_correlation.py sample_incidents.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
kafka_lag:us-east: INC-101,INC-103
```

The sample supplies these fields. `incident_id`, `service`, `signal`, `region`, `severity`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
