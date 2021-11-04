from collections import Iterable
from C1_order_system.datastore import CustomerDataStore, StockDataStore, OrderDataStore, DataFactory
import C1_order_system.datamodel as dm
from C1_order_system.datamodel import OrderItem

class DataFactory:
    """
    class that defines a factory to create objects from imported data
    """

    def __init__(self, _customer_ds: CustomerDataStore, _stock_ds: StockDataStore, _order_ds: OrderDataStore):
        """
        Constructor
        :param _customer_ds: dependency injected for CustomerDataStore instance
        :param _stock_ds: dependency injected for StockDataStore instance
        :param _order_ds: dependency injected for OrderDataStore instance
        """
        # print(f'DataFactory singleton instantiated')
        self.__customer_ds = _customer_ds   # private, final, cannot be altered
        self.__stock_ds = _stock_ds
        self.__order_ds = _order_ds

    def import_customers(self, _customers: []) -> DataFactory:
        if isinstance(_customers, Iterable):
            # iterate over tuple lists in 'list comprehension' style
            [self.__add_customer_from_tuple(_t) for _t in _customers]
        return self

    def import_stock(self, _stock: []) -> DataFactory:
        # TODO:
        if isinstance(_stock, Iterable):
            [self.__add_stock_from_tuple(_t) for _t in _stock]
        return self

    def import_orders(self, _orders: []) -> DataFactory:
        # TODO:
        if isinstance(_orders, Iterable):
            [self.__add_order_from_tuple(_t) for _t in _orders]
        return self

    def __add_customer_from_tuple(self, _t: ()):
        # sample tuple: (505101, 'Abraham Paul', '840 E Dana St, CA 94041 Mountain View', '1-864-259-3252')
        if len(_t) >= 3:
            _customer_id = int(_t[0])       # cast to int (to make sure it's int)
            _name = str(_t[1])
            _address = str(_t[2])
            _phone = str(_t[3])
            _customer_entity = dm.Customer(_customer_id, _name, _address, _phone)
            self.__customer_ds.add_customer(_customer_entity)

    def __add_stock_from_tuple(self, _t: ()):
        # sample tuple: ('0931C010', 'EOS 1D X Mark II Gehäuse', 6299.0, 2, 'Digitale Spiegelreflexkameras')
        # TODO:
        if len(_t) >= 3:
            _sku = str(_t[0])
            _description = str(_t[1])
            _price = int(_t[2])
            _units_available = int(_t[3])
            _stock_entity = dm.Stock(_sku, _description, _price, _units_available)
            self.__stock_ds.add_stock(_stock_entity)

    def __add_order_from_tuple(self, _t: ()):
        # sample tuple: ('00-937-09641', 714268, '2520A015', 1, 'EF 135mm f/2L USM ')
        # TODO:
        if len(_t) >= 3:
            _id = str(_t[0])
            _customer_id = int(_t[1])
            _sku = str(_t[2])
            _units = int(_t[3])
            _description = str(_t[4])
            _order_entity = dm.Order(_id, _customer_id, OrderItem(_sku, _units), _description)
            self.__order_ds.add_order(_order_entity)