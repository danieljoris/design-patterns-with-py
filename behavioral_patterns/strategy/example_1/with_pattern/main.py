from invoice import Invoice
from invoice_tax_calculator import InvoiceTaxCalculator
from tax_strategies.cofins_tax_strategy import CofinsTaxStrategy
from tax_strategies.icms_tax_strategy import IcmsTaxStrategy
from tax_strategies.iss_tax_strategy import IssTaxStrategy
from tax_strategies.pis_tax_strategy import PisTaxStrategy

if __name__ == '__main__':
    tax_calculator = InvoiceTaxCalculator()
    invoice = Invoice(500)
    iss_strategy, icms_strategy, pis_strategy, cofins_strategy = IssTaxStrategy(), IcmsTaxStrategy(), PisTaxStrategy(), CofinsTaxStrategy(),

    print(f"ISS: {tax_calculator.calculate(invoice, iss_strategy)}")
    print(f"ICMS: {tax_calculator.calculate(invoice, icms_strategy)}")
    print(f"PIS: {tax_calculator.calculate(invoice, pis_strategy)}")
    print(f"COFINS: {tax_calculator.calculate(invoice, cofins_strategy)}")
