class Stock:
    """
    class that defines a Stock entity, which can be ordered
    """

    def __init__(self, _id: str, _description: str = "", _price: int = 0, _units_available: int = 0):
        """
        Constructor of class
        :param _id: stock keeping unit (SKU) (private, final, cannot be altered)
        :param _description: description of article or stock unit
        :param _price: price (private, in cent)
        :param _units_available: units available in stock (private)
        :param _category: stock category
        """
        self.__sku = _id     # private, final, cannot be altered
        self.description = _description
        self.__price = self.set_price(_price)                            # private
        self.__units_available = _units_available   # private

    # TODO: complete Class
    def get_sku(self):
        return self.__sku

    def get_price(self):
        return self.__price

    def set_price(self, _price):
        return _price

    def get_units_available(self):
        return self.__units_available

    def has_units_available(self, n):
        return self.__units_available == n

    def transact_units(self, n):
        self.__units_available -= n
