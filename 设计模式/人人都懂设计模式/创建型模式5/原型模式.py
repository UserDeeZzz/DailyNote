"""原型模式 实例化过程复杂 因此直接拷贝属性"""
import copy


class Prototype:

    def clone(self, **attrs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    """
    >>> p1 = Prototype()
    >>> dp = PrototypeDispatcher()
    >>> dp.register("prototype1",p1)
    >>> p2 = p1.clone()
    >>> dp.register("prototype2",p2)
    """

    def __init__(self):
        self.objects = {}

    def get_objects(self):
        return self.objects

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
