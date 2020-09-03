# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  注意: 
# 
#  
#  每个数组中的元素不会超过 100 
#  数组的大小不会超过 200 
#  
# 
#  示例 1: 
# 
#  输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  
# 
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
#  
# 
#  
#  Related Topics 动态规划 
#  👍 346 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        d, v = divmod(sum(nums), 2)
        if v != 0:
            return False
        # 前i个数能否组成和为j
        # 转移方程
        # i-1个数能否组成j以及i-1个数能否组成j-nums[i]
        # base
        length = len(nums)
        dp = [[False] * (d + 1) for _ in range(length)]
        dp[0][0] = True
        for i in range(1, length):
            for j in range(d + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[length - 1][d]
# leetcode submit region end(Prohibit modification and deletion)
