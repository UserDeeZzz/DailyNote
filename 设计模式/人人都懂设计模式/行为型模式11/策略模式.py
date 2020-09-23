from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data):
        pass


class StrategyA(Strategy):

    def do_algorithm(self, data):
        data.sort()


class StrategyB(Strategy):

    def do_algorithm(self, data):
        data.sort(reverse=True)


class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def handle(self, data):
        self._strategy.do_algorithm(data)
        print(",".join(data))


def main():
    """
    >>> a = StrategyA()
    >>> b = StrategyB()
    >>> c= Context(a)
    >>> c.handle(["a","b","c"])
    a,b,c
    >>> c.strategy = b
    >>> c.handle(["a","b","c"])
    c,b,a
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
