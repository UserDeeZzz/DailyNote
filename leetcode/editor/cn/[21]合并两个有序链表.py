# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1261 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = None
        while l1 or l2:
            if not l1 or l2 and l2.val < l1.val:
                val, l2 = l2.val, l2.next
            else:
                val, l1 = l1.val, l1.next

            if head is not None:
                head.next = ListNode(val)
                head = head.next
            else:
                dummy.next = head = ListNode(val)
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
