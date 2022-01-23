
from invoice import Invoice
from invoice_tax_strategy import InvoiceTaxStrategy


class CofinsTaxStrategy(InvoiceTaxStrategy):

    def calculate(self, invoice: Invoice) -> float:
        return invoice.value * 0.04
