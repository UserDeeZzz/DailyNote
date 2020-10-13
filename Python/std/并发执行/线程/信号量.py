import threading
import time

value = 0
# 内部维护一个计数器 acquire -1 release + 1 当计数器等于0 acquire阻塞
# Semaphore 可以无限被释放
# BoundedSemaphore 计数器最大为设定的值 避免无限释放的错误
# sema = threading.Semaphore(1)
sema = threading.BoundedSemaphore(1)


def work():
    global value
    with sema:
        new = value + 1
        time.sleep(0.001)
        value = new


thread_group = [threading.Thread(target=work) for _ in range(1000)]

for t in thread_group:
    t.start()

for t in thread_group:
    t.join()

print(value)
