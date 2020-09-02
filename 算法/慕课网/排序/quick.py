"""快速排序 nlogn nlogn 不稳定"""
from util import random_list


def quick(array):
    length = len(array)
    if length <= 1:
        return array
    left = cursor = 0
    right = length - 1

    while cursor <= right:
        if array[cursor] == array[left]:
            cursor += 1
        elif array[cursor] > array[left]:
            array[cursor], array[right] = array[right], array[cursor]
            right -= 1
        else:
            array[cursor], array[left] = array[left], array[cursor]
            left += 1
            cursor += 1
    return quick(array[:left]) + array[left:cursor] + quick(array[cursor:])


if __name__ == '__main__':
    l = random_list()
    print(quick(l))
