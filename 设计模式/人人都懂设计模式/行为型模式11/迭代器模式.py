"""
不同的方式来遍历整个整合对象
"""


class NumberWords:
    """
    迭代器
    >>> for i in NumberWords(1,2):
    ...     print(i)
    one
    two
    >>> for i in NumberWords(1,3):
    ...     print(i)
    one
    two
    three
    """

    _WORD_MAP = (
        "one",
        "two",
        "three",
        "four",
        "five"
    )

    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end or self.start > len(self._WORD_MAP):
            raise StopIteration

        current = self.start
        self.start += 1
        return self._WORD_MAP[current - 1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()