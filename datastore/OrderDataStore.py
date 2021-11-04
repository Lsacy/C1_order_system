from C1_order_system.datamodel import Order


class OrderDataStore:
    """
    class that defines a container to hold Order objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        # print(f'OrderDataStore singleton instantiated')
        self.__data = {}

    def size(self) -> int:
        return len(self.__data)

    def find_all_orders(self) -> []:
        return list(self.__data.values())

    def add_order(self,_order: Order):
        self.__data[_order.get_id()] = _order

    def remove_order(self,_id: str):
        self.__data.pop(_id, None)

    def find_order_by_id(self, _id: Order):
        return self.__data.get(_id)

    def filter(self, _filter_func: bool) -> [Order]:
        _filtered = list(filter(_filter_func, self.__data.values()))
        return _filtered
