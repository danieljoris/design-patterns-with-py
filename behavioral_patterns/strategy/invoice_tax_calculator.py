
from invoice import Invoice
from invoice_tax_strategy import InvoiceTaxStrategy


class InvoiceTaxCalculator:
    
    def calculate(self, invoice: Invoice, tax_type: InvoiceTaxStrategy) -> float:
        return tax_type.calculate(invoice)

    