"""
共享属性
"""


class Borg:
    __state = {}

    def __init__(self):
        self.__dict__ = self.__state


class YourBorg(Borg):

    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


def main():
    """
    >>> y1 = YourBorg("Running")
    >>> y2 = YourBorg("Relax")
    >>> y1.state
    'Relax'
    >>> assert id(y1) != id(y2)
    >>> y1.age = 20
    >>> getattr(y2,"age")
    20
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
