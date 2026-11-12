# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 incident_correlation.py sample_incidents.csv
kafka_lag:us-east: INC-101,INC-103
test_key_uses_signal_and_region (test_incident_correlation.IncidentCorrelationTest) ... ok
test_returns_only_repeated_clusters (test_incident_correlation.IncidentCorrelationTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
