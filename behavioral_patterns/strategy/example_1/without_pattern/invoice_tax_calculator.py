
from invoice import Invoice


class InvoiceTaxCalculator:
    
    def calculate(self, invoice: Invoice, tax_type) -> float:
        calculated_tax: float = 0
        
        if tax_type == "ISS":
            calculated_tax = invoice.value * 0.1
        elif tax_type == "ICMS":
            calculated_tax = invoice.value * 0.02
        elif tax_type == "PIS":
            calculated_tax = invoice.value * 0.03
        elif tax_type == "COFINS":
            calculated_tax = invoice.value * 0.04
        else:
            calculated_tax = None

        return calculated_tax

    