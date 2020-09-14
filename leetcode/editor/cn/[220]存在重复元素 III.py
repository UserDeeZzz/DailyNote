# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的
# 绝对值也小于等于 ķ 。 
# 
#  如果存在则返回 true，不存在返回 false。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true 
# 
#  示例 2: 
# 
#  输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true 
# 
#  示例 3: 
# 
#  输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false 
#  Related Topics 排序 Ordered Map 
#  👍 226 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 0: return False
        left = right = 0
        buckets = {}
        bucket_size = t + 1
        while right < len(nums):
            # 桶号
            bucket_num = nums[right]//bucket_size
            # 是否在桶中
            if bucket_num in buckets:
                return True
            if bucket_num-1 in buckets and nums[right] - buckets[bucket_num - 1] <= t:
                return True
            if bucket_num+1 in buckets and buckets[bucket_num + 1] - nums[right] <= t:
                return True
            # 放入桶中
            buckets[bucket_num] = nums[right]
            if right - left >= k:
                buckets.pop(nums[left]//bucket_size)
                left += 1
            right += 1

        return False


# leetcode submit region end(Prohibit modification and deletion)
