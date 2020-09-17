# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ， 
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→… 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  示例 1: 
# 
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3. 
# 
#  示例 2: 
# 
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3. 
#  Related Topics 链表 
#  👍 304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next.val}" if self.next else self.val

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:return head
        soft = fast = head
        last = None
        # 偶数偏右 奇数在中间
        while fast and fast.next:
            fast = fast.next.next
            last, soft = soft, soft.next
        if fast is None:  # 偶数偏右
            last.next = None
            mid = soft
        else:  # 奇数在中间
            mid = soft.next
            soft.next = None
        # 翻转后半部分
        mid = self.reverse(mid)
        cur = head
        while mid:
            cur_next = cur.next
            cur.next = mid

            mid_next = mid.next
            mid.next = cur_next

            cur, mid = cur_next, mid_next

    def reverse(self, head):
        last = None
        while head:
            next_node, head.next = head.next, last
            last, head = head, next_node
        return last

        
# leetcode submit region end(Prohibit modification and deletion)
