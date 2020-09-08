# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入："hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  元音字母不包含字母 "y" 。 
#  
#  Related Topics 双指针 字符串 
#  👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
# leetcode submit region end(Prohibit modification and deletion)
