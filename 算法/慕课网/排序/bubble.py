"""冒泡排序 n2 1 稳定"""

import random


def bubble(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def random_list():
    resp = [i for i in range(100)]
    random.shuffle(resp)
    return resp


if __name__ == '__main__':
    rl = random_list()
    print(bubble(rl))
