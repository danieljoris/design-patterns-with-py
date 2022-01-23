
from invoice import Invoice
from invoice_tax_strategy import InvoiceTaxStrategy


class IcmsTaxStrategy(InvoiceTaxStrategy):

    def calculate(self, invoice: Invoice) -> float:
        return invoice.value * 0.02
