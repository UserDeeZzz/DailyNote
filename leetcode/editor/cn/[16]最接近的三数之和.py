# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针 
#  👍 565 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = None
        distance = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                _sum = nums[left] + nums[right] + nums[i]
                if _sum > target:
                    current = _sum - target
                    if current < distance:
                        ans, distance = _sum, current
                    right -= 1
                elif _sum < target:
                    current = target - _sum
                    if current < distance:
                        ans, distance = _sum, current
                    left += 1
                else:
                    ans, distance = _sum,0
                    break
        return ans



# leetcode submit region end(Prohibit modification and deletion)
