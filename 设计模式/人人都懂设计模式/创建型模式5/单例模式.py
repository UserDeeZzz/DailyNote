"""doc string"""
from threading import Lock


class SingleTon:
    _thread_lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._thread_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super().__new__(cls)
        return cls._instance


class T(SingleTon):

    def __init__(self,age):
        self.age = age


if __name__ == '__main__':
    t1 = T(20)
    t2 = T(30)
    print(t1.age)