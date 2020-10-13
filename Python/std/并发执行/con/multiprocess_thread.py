from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


import time


s = time.perf_counter()
# 调用的函数都一样
with ThreadPoolExecutor(max_workers=1) as executor:
    # map chunksize在是进程池时有用
    for res in executor.map(fib, range(25, 38), chunksize=4):
        print(res)
# 调用函数不一样
with ProcessPoolExecutor(max_workers=8) as executor:
    tasks = {executor.submit(fib, i) for i in range(25,38)}
        # executor.submit(fib, 25),
        # executor.submit(fib, 26),
        # executor.submit(pow, 26, 4),
    # }
    for future in as_completed(tasks):
        try:
            result = future.result()
        except Exception as e:
            print(f"raise Exception {e}")
        else:
            print(result)
e = time.perf_counter()

print(e - s)
