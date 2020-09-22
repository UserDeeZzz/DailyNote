import weakref


class FlyweightMeta(type):

    def __new__(mcs, *args, **kwargs):
        """生成一个类"""
        cls = super().__new__(mcs, *args, **kwargs)
        setattr(cls, "pool", weakref.WeakValueDictionary())
        return cls

    @staticmethod
    def _serialize_params(*args, **kwargs):

        args_list = sorted(list(map(str, args)))
        keys = sorted(kwargs.keys())
        for k in keys:
            args_list.append(k + '=' + str(kwargs[k]))
        key = "".join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        """生成的类被实例化的时候"""
        key = cls._serialize_params(*args, **kwargs)
        pool = getattr(cls, "pool", {})
        instance = pool.get(key)
        if instance is None:
            instance = type.__call__(cls, *args, **kwargs)
            pool[key] = instance
        return instance


class Card2(metaclass=FlyweightMeta):
    def __init__(self, *args, **kwargs):
        print('Init {}: {}'.format(self.__class__, (args, kwargs)))


if __name__ == "__main__":
    instances_pool = getattr(Card2, "pool")
    cm1 = Card2("10", "h", a=1)
    cm2 = Card2("10", "h", a=1)
    cm3 = Card2("10", "h", a=2)

    assert (cm1 == cm2) and (cm1 != cm3)
    assert (cm1 is cm2) and (cm1 is not cm3)
    assert len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

    del cm3
    assert len(instances_pool) == 0
