# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  
# 
#  示例： 
# 
#  给你这个链表：1->2->3->4->5 
# 
#  当 k = 2 时，应当返回: 2->1->4->3->5 
# 
#  当 k = 3 时，应当返回: 3->2->1->4->5 
# 
#  
# 
#  说明： 
# 
#  
#  你的算法只能使用常数的额外空间。 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
#  Related Topics 链表 
#  👍 731 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"{self.val}->{self.next}" if self.next else str(self.val)

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head
        idx = 0
        start = head
        end = head
        head = None
        last = None
        while end:
            idx += 1
            if idx % k == 0:
                self.reverse(start, end)
                if head is None:
                    head = end
                else:
                    last.next = end
                last = start
                start = end = start.next
            else:
                end = end.next
        return head

    def reverse(self, start, end):
        prev, cur = start, start.next
        while cur != end:
            next_code, cur.next = cur.next, prev
            prev, cur = cur, next_code
        start.next = cur.next
        cur.next = prev



# leetcode submit region end(Prohibit modification and deletion)
