"""原型模式 实例化过程复杂 因此直接拷贝属性"""
import copy


class Prototype:

    def clone(self, **attrs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:

    def __init__(self):
        self.objects = {}

    def get_objects(self):
        return self.objects

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]


if __name__ == '__main__':
    a = Prototype()
    setattr(a, 'name', [1, 2, 3, [1, 2]])
    print(a.name)
    b = a.clone()
    b.name.append(4)
    print(b.name)
    print(a.name)
