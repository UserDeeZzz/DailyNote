"""归并排序 nlogn n 稳定"""
from util import random_list


def merge(array):
    length = len(array)
    if length < 2:
        return array
    mid = length//2
    return helper(merge(array[:mid]),merge(array[mid:]))



def helper(arr1,arr2):
    resp = []
    while arr1 or arr2:
        if not arr1 or arr2 and arr2[0] < arr1[0]:
            resp.append(arr2.pop(0))
        else:
            resp.append(arr1.pop(0))
    return resp

if __name__ == '__main__':
    l = random_list()
    print(merge(l))
