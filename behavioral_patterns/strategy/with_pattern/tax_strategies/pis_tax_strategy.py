from invoice import Invoice
from invoice_tax_strategy import InvoiceTaxStrategy


class PisTaxStrategy(InvoiceTaxStrategy):

    def calculate(self, invoice: Invoice) -> float:
        return invoice.value * 0.03
