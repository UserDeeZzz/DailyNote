# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针 
#  👍 610 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        while p2 >= 0:
            if p1 < 0 or nums1[p1] < nums2[p2]:
                nums1[p2 + p1 + 1] = nums2[p2]
                p2 -= 1
            else:
                nums1[p2 + p1 + 1] = nums1[p1]
                p1 -= 1
        return

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5)
    print(res)
