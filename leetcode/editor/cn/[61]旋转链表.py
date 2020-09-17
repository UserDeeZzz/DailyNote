# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#  
# 
#  示例 2: 
# 
#  输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL 
#  Related Topics 链表 双指针 
#  👍 334 👎 0


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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0: return head
        dummy = ListNode(-1)
        dummy.next = head
        # 计算链表长度
        length = 1
        while head.next:
            head = head.next
            length += 1
        # 尾指针
        tail = head
        # 闭环
        tail.next = dummy.next
        # 右转相当于头指针逆时针旋转
        # 逆时针旋转k 相当于顺时针旋转 length - k
        idx = 0
        k = k % length
        while idx < length - k:
            dummy.next = dummy.next.next
            tail = tail.next
            idx += 1
        tail.next = None
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
