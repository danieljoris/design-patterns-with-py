from invoice import Invoice
from invoice_tax_strategy import InvoiceTaxStrategy


class IssTaxStrategy(InvoiceTaxStrategy):

    def calculate(self, invoice: Invoice) -> float:
        return invoice.value * 0.01
