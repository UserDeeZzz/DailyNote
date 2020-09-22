"""
对象池 构件对象是io操作 因此复用
"""
import queue


class ObjectPool:
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    q = queue.Queue(maxsize=5)
    with ObjectPool(q) as obj:
        print(obj)

    with ObjectPool(q) as obj:
        print(obj)
