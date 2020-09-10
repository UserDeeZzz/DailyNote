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


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        # 先排序，关键！
        nums.sort()
        ans = set()
        N, target = 3, 0
        self._find_sum(nums, 0, N, target, [], ans)
        return list(ans)

    def _find_sum(self, nums, start, N, target, path, ans):
        # terminator
        if len(nums) < N or N < 2: return
        # process
        if N == 2:
            # 两数求和
            d = set()
            for j in range(start, len(nums)):
                if target - nums[j] in d:
                    ans.add(tuple(path + [target - nums[j], nums[j]]))
                else:
                    d.add(nums[j])
        else:
            for i in range(start, len(nums)):
                # 剪枝1: target比剩余数字能组成的最小值还要小 或 比能组成的最大值还要大，就可以停止循环了
                if target < nums[i] * N or target > nums[-1] * N: break
                # 剪枝2: 去重
                if i > start and nums[i] == nums[i - 1]: continue
                # drill down
                self._find_sum(nums, i + 1, N - 1, target - nums[i], path + [nums[i]], ans)
        return

# leetcode submit region end(Prohibit modification and deletion)
