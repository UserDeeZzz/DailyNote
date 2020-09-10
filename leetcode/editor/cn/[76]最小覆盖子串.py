# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。 
# 
#  
# 
#  示例： 
# 
#  输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC" 
# 
#  
# 
#  提示： 
# 
#  
#  如果 S 中不存这样的子串，则返回空字符串 ""。 
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 738 👎 0

from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 缓存
        cache = defaultdict(int)
        sl = len(s)
        for i in t:
            cache[i] += 1
        # 满足条件
        need = len(cache)
        # 滑窗
        window = defaultdict(int)
        left = right = 0
        # 最小情况
        res = ""
        while right < sl:
            if s[right] in cache:
                window[s[right]] += 1
                if window[s[right]] == cache[s[right]]:
                    need -= 1
                    while need == 0:
                        if s[left] in cache:
                            window[s[left]] -= 1
                            if window[s[left]] < cache[s[left]]:
                                need += 1
                                if not res or right + 1 - left < len(res):
                                    res = s[left:right + 1]
                        left += 1
            right += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
