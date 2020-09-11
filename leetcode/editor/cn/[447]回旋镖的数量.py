# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺
# 序）。 
# 
#  找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。 
# 
#  示例: 
# 
#  
# 输入:
# [[0,0],[1,0],[2,0]]
# 
# 输出:
# 2
# 
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#  
#  Related Topics 哈希表 
#  👍 103 👎 0

from collections import defaultdict
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        account = 0
        for i in range(len(points)):
            cache = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                cache[dis] += 1
            for v in cache.values():
                if v >= 2: account += v * (v - 1)
        return account


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    points = [[0, 0], [1, 0], [2, 0]]
    o = Solution()
    o.numberOfBoomerangs(points)
