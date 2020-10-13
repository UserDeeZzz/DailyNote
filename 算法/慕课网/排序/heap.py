"""
    堆排序 nlogn 1
    按层序遍历顺序组织堆
    利用最左侧点等于2的k次方-1 k是深度 深度从0开始
    总结点数2的k次方-1 k是深度 深度从1开始
    完全二叉树 i的左子结点 2i+1 右子结点2i+2
"""

from util import random_list


def heap_sort(array):
    length = len(array)

    def heapify(a, j):
        """
            2i+1 =< length-1 <= 2i+2
            2i+2 =< length <= 2i+3
            length//2 = i+1
            i = length//2 -1
            从大到小依次判断节点
        """
        left = 2 * j + 1
        right = 2 * j + 2
        largest = j

        if left < length and a[left] > a[largest]:
            largest = left
        if right < length and a[right] > a[largest]:
            largest = right

        if largest != j:
            a[j], a[largest] = a[largest], a[j]
            # 因为交换了顺序,下面的要重新调整
            heapify(a, largest)

    # 初始化堆 从下往上
    for i in range(length // 2 - 1, -1, -1):
        heapify(array, i)
    # 排序
    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        length -= 1
        # 因为下面都调整过了 满足堆定义 因此只需调整0 从上往下
        heapify(array, 0)
    return array


if __name__ == '__main__':
    l = random_list()
    print(heap_sort(l))
