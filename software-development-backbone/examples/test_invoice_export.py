import csv
from io import StringIO
import unittest
from invoice_demo.application import export_invoices
from invoice_demo.infrastructure import MemoryInvoiceRepository


class InvoiceExportTests(unittest.TestCase):
    def setUp(self):
        self.repository = MemoryInvoiceRepository([
            {"id": 1, "amount": "10.00"},
            {"id": 2, "amount": "25.00"},
        ])
        self.audit = []

    def test_selected_invoices_become_csv(self):
        result = export_invoices(self.repository, [2], "finance", self.audit)
        rows = list(csv.DictReader(StringIO(result)))
        self.assertEqual(rows, [{"id": "2", "amount": "25.00"}])

    def test_export_requires_finance_role(self):
        with self.assertRaises(PermissionError):
            export_invoices(self.repository, [2], "guest", self.audit)
        self.assertEqual(self.audit, [])

    def test_success_records_audit_event(self):
        export_invoices(self.repository, [2], "finance", self.audit)
        self.assertEqual(self.audit, [
            {"action": "invoice_export", "ids": [2]},
        ])


if __name__ == "__main__":
    unittest.main()
