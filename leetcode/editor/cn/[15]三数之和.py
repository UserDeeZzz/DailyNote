# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2562 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # 排序
        nums.sort()
        # 求解n个数总和为0
        return self.nSum(nums, 3, 0)

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
