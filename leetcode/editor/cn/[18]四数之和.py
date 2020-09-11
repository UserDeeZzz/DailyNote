# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针 
#  👍 564 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        return self.nSum(nums, 4, target)

    def twoSum(self, nums, target):
        cache = {}
        res = set()
        for i, v in enumerate(nums):
            idx = cache.get(target - v)
            if idx is not None:
                res.add((target - v, v))
            cache[v] = i
        return [list(i) for i in res]

    def nSum(self, nums, n, target):
        res = []
        if len(nums) < n:
            return res
        if n == 2:
            res = self.twoSum(nums, target)
        else:
            for i in range(len(nums)):
                # 连续相同 必定重复
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                # 递增 小于最小值×n 大于最大值×n
                if target < nums[i] * n or target > nums[-1] * n:
                    break
                # 递归
                ans = self.nSum(nums[i + 1:], n - 1, target - nums[i])
                for a in ans:
                    a.insert(0, nums[i])
                    res.append(a)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = [1, -2, -5, -4, -3, 3, 3, 5]
    o = Solution()
    print(o.fourSum(s, -11))
