import threading
import time

value = 0

# def work():
#     global value
#     new = value + 1
#     time.sleep(0.001)
#     # 执行赋值操作时切换线程就会导致少加1
#     value = new
lock = threading.Lock()


def work():
    global value
    # lock.acquire()
    #
    # new = value + 1
    # time.sleep(0.001)
    # # 执行赋值操作时切换线程就会导致少加1
    # value = new
    #
    # lock.release()

    with lock:
        new = value + 1
        time.sleep(0.001)
        # 执行赋值操作时切换线程就会导致少加1
        value = new


thread_groups = [threading.Thread(target=work) for _ in range(1000)]

for t in thread_groups:
    t.start()

for t in thread_groups:
    t.join()

print(value)
