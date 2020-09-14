# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。 
# 
#  示例 1: 
# 
#  输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#  
# 
#  示例 2: 
# 
#  输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6 
#  Related Topics 哈希表 数学 
#  👍 179 👎 0
from typing import List
from collections import defaultdict, Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """斜率精度 点自成线 """
        from decimal import Decimal
        if not points: return 0
        # 去重 计点数
        counter = Counter(((x, y) for x, y in points))
        # 点自成直线
        ans = counter.most_common(1)[0][1]
        visited = defaultdict(set)  # 缓存直线 点
        cache = defaultdict(int)
        keys = list(counter.keys())
        # 遍历点
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i][0] - keys[j][0]:
                    a = Decimal(keys[i][1] - keys[j][1]) / Decimal(keys[i][0] - keys[j][0])  # 斜率
                    b = Decimal(keys[i][1]) - Decimal(keys[i][0]) * a  # 截距
                    key = (a, b)
                else:
                    # x = n
                    key = keys[i][0]

                for item in (keys[i], keys[j]):
                    if item not in visited[key]:
                        cache[key] += counter[item]
                        visited[key].add(item)

                ans = max(cache[key], ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    points = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
    o = Solution()
    print(o.maxPoints(points))
