


if __name__ == '__main__':
    from invoice import Invoice
    from invoice_tax_calculator import InvoiceTaxCalculator

    tax_calculator = InvoiceTaxCalculator()
    invoice = Invoice(500)

    iss_tax_result = tax_calculator.calculate(invoice, "ISS")
    icms_tax_result = tax_calculator.calculate(invoice, "ICMS")
    pis_tax_result = tax_calculator.calculate(invoice, "PIS")
    cofins_tax_result = tax_calculator.calculate(invoice, "COFINS")

    print(f"ISS: {iss_tax_result}")
    print(f"ICMS: {icms_tax_result}")
    print(f"PIS: {pis_tax_result}")
    print(f"COFINS: {cofins_tax_result}")
