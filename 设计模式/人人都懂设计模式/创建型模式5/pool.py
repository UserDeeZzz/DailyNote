"""
对象池 构件对象是io操作 因此复用
"""
import queue


class Pool:

    def __init__(self):
        self.queue = queue.Queue()
        self.item = None

    def __enter__(self):
        return self.queue.get()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.queue.put(self.item)

    def __del__(self):
        self.queue.put(self.item)

