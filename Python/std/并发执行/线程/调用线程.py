import threading
import time


def work(second):
    count = 0
    while count < 5:
        time.sleep(second)
        count += 1
        # 获取当前线程
        print(f"{threading.current_thread().name} {time.time()}")
        print(f"当前存活线程{threading.active_count()}")
        print(f"当前存活线程{threading.enumerate()}")


# 默认daemon=False 继承自创建他的线程
# 如果daemon=True 守护线程 daemon=False 非守护线程
# 当剩余的线程都是守护线程 退出主线程 程序退出
thread_groups = [threading.Thread(target=work, args=(10,), name=f"thread--{i}", daemon=False) for i in range(2)]

for t in thread_groups:
    t.start()  # 调用run方法 启动线程

for t in thread_groups:
    t.join(timeout=2)  # 阻塞主线程 直到线程结束或超时

print(f'{threading.main_thread()} exit...')
