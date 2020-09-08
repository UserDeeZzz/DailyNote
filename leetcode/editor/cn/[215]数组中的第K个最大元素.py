# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  示例 1: 
# 
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  说明: 
# 
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
#  Related Topics 堆 分治算法 
#  👍 691 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def heapify(self, nums, i, length):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left <= length and nums[left] > nums[largest]:
            largest = left
        if right <= length and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(nums, largest, length)

    def build_heap(self, nums, length):
        # i的孩子 2i+1 2i+2
        # 最大非叶节点  length//2 - 1
        for i in range(length // 2 - 1, -1, -1):
            self.heapify(nums, i, length - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        self.build_heap(nums, length)
        for i in range(1, k + 1):
            nums[0], nums[length - i] = nums[length - i], nums[0]
            self.heapify(nums, 0, length - i - 1)
        return nums[length - k]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
