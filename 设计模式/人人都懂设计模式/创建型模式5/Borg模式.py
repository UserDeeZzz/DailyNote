"""
共享属性
"""


class Borg:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__state"):
            setattr(cls, "__state", {})
        obj = super().__new__(cls)
        obj.__dict__ = getattr(cls, "__state")
        return obj


class YourBorg(metaclass=Borg):
    """
    >>> y1 = YourBorg("Running")
    >>> y2 = YourBorg("Relax")
    >>> y1.state
    Relax
    >>> assert id(y1) != id(y2)
    >>> y1.age = 20
    >>> getattr(y2,"age")
    None
    """

    def __init__(self, state):
        self.state = state


if __name__ == '__main__':
    import doctest

    doctest.testmod()
