import unittest

from incident_correlation import clusters, correlation_key


class IncidentCorrelationTest(unittest.TestCase):
    def test_key_uses_signal_and_region(self):
        row = {"signal": "kafka_lag", "region": "us-east"}
        self.assertEqual(correlation_key(row), "kafka_lag:us-east")

    def test_returns_only_repeated_clusters(self):
        rows = [
            {"incident_id": "1", "signal": "kafka_lag", "region": "us-east"},
            {"incident_id": "2", "signal": "kafka_lag", "region": "us-east"},
            {"incident_id": "3", "signal": "latency", "region": "us-west"},
        ]
        self.assertEqual(clusters(rows)[0]["incident_ids"], ["1", "2"])


if __name__ == "__main__":
    unittest.main()
