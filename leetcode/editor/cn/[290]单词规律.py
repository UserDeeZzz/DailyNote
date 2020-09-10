# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。 
# 
#  这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。 
# 
#  示例1: 
# 
#  输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true 
# 
#  示例 2: 
# 
#  输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false 
# 
#  示例 4: 
# 
#  输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false 
# 
#  说明: 
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 
#  Related Topics 哈希表 
#  👍 187 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        l = str.split(' ')
        if len(l) != len(pattern):
            return False
        ks = {}
        vs = {}
        for i in range(len(pattern)):
            if pattern[i] not in ks and l[i] not in vs:
                ks[pattern[i]] = l[i]
                vs[l[i]] = pattern[i]
            elif pattern[i] in ks and l[i] in vs:
                if ks[pattern[i]] != l[i] or vs[l[i]] != pattern[i]:
                    return False
            else:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    p = "abba"
    s = "dog cat cat dog"
    o.wordPattern(p, s)
