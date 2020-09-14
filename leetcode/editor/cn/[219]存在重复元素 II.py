# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值
#  至多为 k。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,2,3,1], k = 3
# 输出: true 
# 
#  示例 2: 
# 
#  输入: nums = [1,0,1,1], k = 1
# 输出: true 
# 
#  示例 3: 
# 
#  输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false 
#  Related Topics 数组 哈希表 
#  👍 197 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        window = set()
        while right < len(nums):
            # 判断当前是否存在
            if nums[right] in window:
                return True
            else:
                window.add(nums[right])
            right += 1
            if right - left > k:
                window.remove(nums[left])
                left += 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    print(o.containsNearbyDuplicate([1, 0, 1, 1], 1))
