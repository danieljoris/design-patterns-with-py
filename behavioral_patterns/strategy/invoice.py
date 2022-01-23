
class Invoice:

    def __init__(self, value: float) -> None:
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    