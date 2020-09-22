"""
组合是一种结构型设计模式， 你可以使用它将对象组合成树状结构， 并且能像使用独立对象一样使用它们
"""
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):

    @abstractmethod
    def render(self):
        pass


class CompositeGraphic(Graphic):

    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)

    def render(self):
        for g in self.graphics:
            g.render()


class Ellipse(Graphic):

    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Ellipse: {self.name}")


def main():
    """
    >>> e1 = Ellipse(1)
    >>> e2 = Ellipse(2)
    >>> e3 = Ellipse(3)
    >>> e4 = Ellipse(4)
    >>> cp1 = CompositeGraphic()
    >>> cp2 = CompositeGraphic()
    >>> cp = CompositeGraphic()
    >>> cp1.add(e1)
    >>> cp1.add(e2)
    >>> cp2.add(e3)
    >>> cp2.add(e4)
    >>> cp.add(cp1)
    >>> cp.add(cp2)
    >>> cp.render()
    Ellipse: 1
    Ellipse: 2
    Ellipse: 3
    Ellipse: 4
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
