"""使用多个简单的对象一步一步构建成一个复杂的对象"""
from abc import ABCMeta, abstractmethod


class Building(metaclass=ABCMeta):

    def __init__(self, ):
        """
        将复杂的初始化过程分步
        """
        self.size = self.build_size()
        self.floor = self.build_floor()

    @abstractmethod
    def build_floor(self):
        pass

    @abstractmethod
    def build_size(self):
        pass

    def __repr__(self):
        return f"Floor: {self.floor} | Size: {self.size}"


class House(Building):
    """
    >>> h = House()
    >>> h
    Floor: One | Size: Big
    """
    def build_floor(self):
        return "One"

    def build_size(self):
        return "Big"


class Flat(Building):
    """
    >>> f = Flat()
    >>> f
    Floor: Two | Size: Small
    """
    def build_floor(self):
        return "Two"

    def build_size(self):
        return "Small"


if __name__ == '__main__':
    import doctest

    doctest.testmod()
