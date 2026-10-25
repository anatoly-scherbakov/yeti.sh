class MemoryInvoiceRepository:
    def __init__(self, rows):
        self.rows = rows

    def selected(self, identifiers):
        return [row for row in self.rows if row["id"] in identifiers]
