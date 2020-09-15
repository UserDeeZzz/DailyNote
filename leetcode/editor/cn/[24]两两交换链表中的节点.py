# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表 
#  👍 622 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        last = dummy
        dummy.next = head
        while head and head.next:
            next_head = head.next  # 2
            last.next = next_head  # -2
            head.next = next_head.next # 1-3
            next_head.next = head # 2-1

            head, last = head.next, head
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
