from threading import Lock


class SingleTon:
    _thread_lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._thread_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)
        return cls._instance


class T(SingleTon):
    """
    >>> t1 = T(20)
    >>> t2 = T(30)
    >>> t1.age
    30
    """

    def __init__(self, age, name=None):
        self.age = age
        self.name = name


if __name__ == '__main__':
    import doctest

    doctest.testmod()
