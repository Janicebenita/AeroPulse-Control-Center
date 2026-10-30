import unittest
from agent import analyze_disruption


class DisruptionTests(unittest.TestCase):
    def test_maintenance_flag_is_critical_and_cited(self):
        result = analyze_disruption({"flight_id": "AP1", "maintenance_flags": ["hydraulics"]})
        self.assertEqual(result["severity"], "critical")
        self.assertTrue(any(item["field"] == "maintenance_flags" for item in result["evidence"]))


if __name__ == "__main__":
    unittest.main()
