# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针 
#  👍 636 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pre, slow, fast = None, head, head
        # 找到中点并且翻转
        while fast and fast.next:
            fast = fast.next.next
            temp = pre
            pre, slow = slow, slow.next
            pre.next = temp
        if fast:
            slow = slow.next
        # 对比
        while pre and pre.val == slow.val:
            slow = slow.next
            pre = pre.next
        return not pre


# leetcode submit region end(Prohibit modification and deletion)
