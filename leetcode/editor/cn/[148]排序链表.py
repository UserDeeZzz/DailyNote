# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。 
# 
#  示例 1: 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2: 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5 
#  Related Topics 排序 链表 
#  👍 736 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        # 快慢指针找到中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, n1, n2):
        p = dummy = ListNode(-1)
        while n1 and n2:
            if n1.val < n2.val:
                p.next, n1 = n1, n1.next
            else:
                p.next, n2 = n2, n2.next
            p = p.next
        p.next = n1 or n2
        return dummy.next
        
# leetcode submit region end(Prohibit modification and deletion)
