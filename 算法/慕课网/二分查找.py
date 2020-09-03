"""二分查找"""


def binary_search(array, num):
    if not array:
        return False
    mid = len(array) // 2
    if array[mid] < num:
        return binary_search(array[mid + 1:], num)
    elif array[mid] > num:
        return binary_search(array[:mid], num)
    else:
        return True


if __name__ == '__main__':
    print(binary_search([1, 2, 3], 3))
