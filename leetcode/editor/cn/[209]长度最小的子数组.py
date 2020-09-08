# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回
#  0。 
# 
#  
# 
#  示例： 
# 
#  输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。 
#  
#  Related Topics 数组 双指针 二分查找 
#  👍 430 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        min_length = 0
        account = nums[0]
        length = len(nums)
        while left <= right:
            if account < s:
                right += 1
                if right == length:
                    break
                if nums[right] == s:
                    return 1
                account += nums[right]
            else:
                min_length = min(min_length, right - left+1) if min_length != 0 else right - left+1
                account -= nums[left]
                left += 1
        return min_length
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    o = Solution()
    o.minSubArrayLen(s,nums)