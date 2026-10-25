import csv
from io import StringIO
from invoice_demo.domain import InvoiceRepository


def export_invoices(repository: InvoiceRepository, identifiers, role, audit):
    if role != "finance":
        raise PermissionError("Finance role required")
    rows = repository.selected(identifiers)
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "amount"])
    writer.writeheader()
    writer.writerows(rows)
    audit.append({"action": "invoice_export", "ids": identifiers})
    return output.getvalue()
