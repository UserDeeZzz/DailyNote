# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 270 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        right = length - 1
        left = 0
        while left <= right:
            while not s[left].isdigit() and not s[left].isalnum():
                if left < right:
                    left += 1
                else:
                    return True
            while not s[right].isdigit() and not s[right].isalnum():
                if right > left:
                    right -= 1
                else:
                    return True
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().isPalindrome(""))
