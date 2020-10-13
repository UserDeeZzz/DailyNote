import threading
import time

lock = threading.RLock()

value = 0


def f():
    with lock:
        g()
        h()


def g():
    with lock:
        h()
        global value
        new = value + 1
        time.sleep(0.001)
        value = new


def h():
    with lock:
        global value
        new = value + 1
        time.sleep(0.001)
        value = new


thread_groups = [threading.Thread(target=f) for _ in range(1000)]

for t in thread_groups:
    t.start()

for t in thread_groups:
    t.join()

print(value)
