"""选择排序 n2 1 不稳定"""
from util import random_list


def choice(array):
    length = len(array)
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[min_idx], array[i] = array[i], array[min_idx]
    return array


if __name__ == '__main__':
    l = random_list()
    print(choice(l))
