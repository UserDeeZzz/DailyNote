# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  示例 1: 
# 
#  输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4. 
# 
#  示例 2: 
# 
#  输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9. 
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 593 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, n + 1):  # 和
            for j in range(2, int(math.sqrt(i)) + 1):  # j平方数
                dp[i] = min(dp[i - j * j] + 1, dp[i])
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    print(o.numSquares(12))
