
from abc import ABC, abstractclassmethod

from invoice import Invoice


class InvoiceTaxStrategy(ABC):

    @abstractclassmethod
    def calculate(self, invoice: Invoice) -> float:
        pass
