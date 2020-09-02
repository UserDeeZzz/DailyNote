"""冒泡排序 n2 1 稳定"""
from util import random_list


def bubble(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    rl = random_list()
    print(bubble(rl))
