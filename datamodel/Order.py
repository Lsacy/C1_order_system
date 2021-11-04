from datetime import datetime

class OrderItem:
    def __init__(self, _sku: str, _units: int):
        """
        Constructor
        :param _sku: ordered item as stock keeping unit (SKU) id in Stock
        :param _units: ordered units
        """
        self.__sku = _sku       # private, final attribute, cannot be altered
        self.units = _units

    def get_sku(self):
        return self.__sku

class Order:
    """
    class that defines an Order entity, which represents a transaction
    between a selling business and a Customer
    """

    def __init__(self, _id: str, _customer_id: int, _items: [OrderItem], _description: str, _date: datetime = datetime.now()):
        """
        Constructor
        :param _id: stock keeping unit (SKU) (private, final, cannot be altered)
        :param _description: description of article or stock unit
        :param _price: price (private, in cent)
        :param _units_available: units available in stock (private)
        :param _category: stock category
        """
        self.__id = _id                     # private, final attribute, cannot be altered
        self.__customer_id = _customer_id
        self.__items = [_items]
        self._description = _description
        self.__date = _date

    def get_id(self):
        return self.__id

    def get_customer_id(self):
        return self.__customer_id

    def get_date(self):
        return self.__date

    def add_item(self, _sku: str, _units: int):
        _item = OrderItem(_sku, _units)
        self.__items.append(_item)
        return len(self.items_count())

    def items_count(self):
        return len(self.__items)

    def get_item(self, _i):
        return self.__items[_i] if 0 <= _i < self.items_count() else None



