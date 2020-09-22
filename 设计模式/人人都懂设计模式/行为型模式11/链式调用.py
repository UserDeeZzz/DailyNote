"""
代码可读性好 orm
"""


class ChainMethod:
    """
    >>> cm = ChainMethod()
    >>> cm.get().filter(3,6).all()
    [3, 4, 5, 6]
    """

    def __init__(self):
        self.cache = []

    @staticmethod
    def query_db():
        return [i for i in range(10)]

    def get(self):
        self.cache = self.query_db()
        return self

    def filter(self, s, e):
        self.cache = list(filter(lambda x: s <= x <= e, self.cache))
        return self

    def all(self):
        return self.cache


if __name__ == '__main__':
    import doctest

    doctest.testmod()
