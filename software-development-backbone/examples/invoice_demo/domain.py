from typing import Protocol


class InvoiceRepository(Protocol):
    def selected(self, identifiers: list[int]) -> list[dict]: ...
