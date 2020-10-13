import random
import threading
import time
import itertools

event = threading.Event()

q = []


def producer(l):
    while 1:
        item = random.randint(10, 100)
        l.append(item)
        print(f"生产元素:{item}")
        # 事件发生
        event.set()
        time.sleep(1)


def consumer(l):
    while 1:
        # 事件是否发生
        flag = event.is_set()
        if flag:
            try:
                item = l.pop()
                print(f"消费元素:{item}")
                event.clear()
            except IndexError:
                pass


consumers = [threading.Thread(target=consumer, args=(q,)) for _ in range(2)]
producers = [threading.Thread(target=producer, args=(q,))]

threads = itertools.chain(consumers, producers)

for t in threads:
    t.start()

for t in threads:
    t.join()
