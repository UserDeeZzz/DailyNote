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
        if not nums: return []
        # 排序
        nums.sort()
        # 求解n个数总和为0
        return self.nSum(nums,3,0,[])

    def nSum(self, nums, n, target, path):
        if len(nums) < n: return []
        if n == 2:
            cache = {}
            for i, v in enumerate(nums):
                if nums[i] > target:
                    return []
                idx = cache.get(target - v)
                if idx is not None:
                    return [[target - v, v]]
                cache[v] = i
            return []
        else:
            res = []
            for i in range(len(nums)):
                # 已经遍历过
                if i in path:
                    continue
                # 已经大于target 后面就不可能等于
                if nums[i] >= target:
                    break
                else:
                    path.append(i)
                    ans = self.nSum(nums[i + 1:], n - 1, target - nums[i], path)
                    for a in ans:
                        res.append([nums[i]]+a)
            return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    o = Solution()
    print(o.threeSum(nums))