from C1_order_system.datamodel import Stock


class StockDataStore:
    """
    class that defines a container to hold Stock objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        # print(f'StockDataStore singleton instantiated')
        self.__data = {}

    def size(self) -> int:
        return len(self.__data)

    def add_stock(self,_stock_unit: Stock):
        self.__data[_stock_unit.get_sku()] = _stock_unit

    def remove_stock(self,_sku: int):
        self.__data.pop(_sku, None)

    def find_stock_by_sku(self,_sku: int):
        return self.__data.get(_sku)

    def find_all_stock(self) -> []:
        return list(self.__data.values())

    def filter(self, _filter_func: bool) -> [Stock]:
        _filtered = list(filter(_filter_func, self.__data.values()))
        return _filtered


