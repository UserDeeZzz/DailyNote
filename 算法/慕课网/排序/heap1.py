"""doc string"""
from util import random_list


def heap_sort(array):
    length = len(array)

    # 堆化

    def heapify(a, j):
        left = 2 * j + 1
        right = 2 * j + 2
        largest = j
        if left < length and a[left] > a[largest]:
            largest = left
        if right < length and a[right] > a[largest]:
            largest = right
        if largest != j:
            a[largest], a[j] = a[j], a[largest]
            heapify(a, largest)

    # 初始化堆
    for i in range(length // 2 - 1, -1, -1):
        heapify(array, i)

    # 排序并调整堆
    for i in range(length - 1, 0, -1):
        length -= 1
        array[0], array[i] = array[i], array[0]
        heapify(array, 0)

    return array


if __name__ == '__main__':
    l = random_list()
    print(heap_sort(l))
