# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 716 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        0的最左边界设定个指针 最右边界就是i
        """
        length = len(nums)
        left = None
        for i in range(length):
            if nums[i] != 0 and left is not None:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            if nums[i] == 0 and left is None:
                left = i


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    array = [1, 0, 0, 3, 12]
    Solution().moveZeroes(array)
    print(array)
