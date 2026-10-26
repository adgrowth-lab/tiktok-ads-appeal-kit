#!/usr/bin/env python3
"""
Unit Test Suite for TikTok Ads Suspension Appeal Field Kit 📨
Zero-dependency test suite validating template variables, file exports, catalogs, and CLI JSON outputs.
"""

import unittest
import subprocess
import json
import tempfile
import os
from appeal import generate_appeal, APPEAL_CATALOG, OFFICIAL_PORTAL, WEB_CALCULATOR


class TestAppealKit(unittest.TestCase):

    def test_unusual_activity_appeal(self):
        res = generate_appeal("unusual-activity", brand="EcoNest Goods", account_id="ADV-883921", website="econest.com")
        self.assertEqual(res["appeal_type"], "unusual-activity")
        self.assertIn("EcoNest Goods", res["subject"])
        self.assertIn("ADV-883921", res["subject"])
        self.assertIn("econest.com", res["body"])
        self.assertGreaterEqual(len(res["required_documents"]), 3)
        self.assertEqual(res["official_portal"], OFFICIAL_PORTAL)

    def test_payment_appeal(self):
        res = generate_appeal("payment", brand="Acme LLC", account_id="ADV-123456")
        self.assertEqual(res["appeal_type"], "payment")
        self.assertIn("PAYMENT VERIFICATION", res["subject"])
        self.assertIn("Acme LLC", res["body"])
        self.assertIn("ADV-123456", res["body"])

    def test_creative_appeal(self):
        res = generate_appeal("creative", brand="Glow Lab", account_id="ADV-998877")
        self.assertEqual(res["appeal_type"], "creative")
        self.assertIn("POLICY COMPLIANCE APPEAL", res["subject"])

    def test_business_center_appeal(self):
        res = generate_appeal("business-center", brand="Horizon Agency", account_id="BC-772211")
        self.assertEqual(res["appeal_type"], "business-center")
        self.assertIn("Business Center", res["name"])

    def test_identity_kyb_appeal(self):
        res = generate_appeal("identity", brand="Apex Direct LLC", account_id="ADV-443322")
        self.assertEqual(res["appeal_type"], "identity")
        self.assertIn("KYB", res["name"])

    def test_invalid_type_fallback(self):
        # Invalid appeal type falls back to unusual-activity
        res = generate_appeal("non-existent-type", brand="Test Brand")
        self.assertEqual(res["appeal_type"], "unusual-activity")

    def test_save_to_file(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".txt") as tf:
            temp_path = tf.name

        try:
            res = generate_appeal("unusual-activity", brand="Saved Brand", output_path=temp_path)
            self.assertEqual(res["saved_file"], temp_path)
            with open(temp_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("Saved Brand", content)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_cli_json_mode(self):
        cmd = ["python3", "appeal.py", "--type", "payment", "--brand", "Cli Brand", "--json"]
        out = subprocess.check_output(cmd, cwd=os.path.dirname(__file__)).decode("utf-8")
        data = json.loads(out)
        self.assertEqual(data["appeal_type"], "payment")
        self.assertIn("Cli Brand", data["body"])
        self.assertEqual(data["official_portal"], OFFICIAL_PORTAL)


if __name__ == "__main__":
    unittest.main()
