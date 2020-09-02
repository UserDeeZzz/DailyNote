"""插入排序 n2 1 稳定"""
from util import random_list


def insert(array):
    length = len(array)
    for i in range(1, length):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array


if __name__ == '__main__':
    l = random_list()
    print(insert(l))
