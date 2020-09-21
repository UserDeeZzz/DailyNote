"""
加快初始化过程 懒加载方式
"""


def lazy_property(fn):
    attr = "_lazy__" + fn.__name__

    @property
    def inner(self, *args, **kwargs):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self, * args, **kwargs))
        return getattr(self, attr)

    return inner


class Person:
    """
    >>> p = Person()
    >>> p.age
    0
    >>> p.parents
    'Father and mother'
    """
    def __init__(self):
        self.age = 0

    @lazy_property
    def parents(self):
        self.age += 1
        return 'Father and mother'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
