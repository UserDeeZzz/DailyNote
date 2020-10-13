import threading
import time


def consumer(cond):
    with cond:
        cond.wait()  # 等待生产者完成
        print(f"consume resource")


def producer(cond):
    with cond:
        time.sleep(1)
        print(f"produce complete")
        cond.notify_all()


condition = threading.Condition()

thread_group = [
    threading.Thread(name='c1', target=consumer, args=(condition,)),
    threading.Thread(name='c2', target=consumer, args=(condition,)),
    threading.Thread(name='p', target=producer, args=(condition,)), ]

for t in thread_group:
    t.start()

for t in thread_group:
    t.join()
