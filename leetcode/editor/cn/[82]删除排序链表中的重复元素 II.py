# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#  
# 
#  示例 2: 
# 
#  输入: 1->1->1->2->3
# 输出: 2->3 
#  Related Topics 链表 
#  👍 364 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"{self.val}->{self.next}" if self.next else str(self.val)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        last = dummy
        while head:
            # 找到下一个不重复的点
            repeat = None
            while head and (head.next and head.val == head.next.val or head.val == repeat):
                repeat = head.val
                head = head.next

            if repeat is None:
                last.next = head
                last, head = head, head.next
            # 结尾
            if head is None:
                last.next = head

        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    n1 = ListNode(1)
    n2 = ListNode(1)
    # n3 = ListNode(3)
    # n4 = ListNode(3)
    # n5 = ListNode(4)
    # n6 = ListNode(4)
    # n7 = ListNode(5)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    # n5.next = n6
    # n6.next = n7
    o = o.deleteDuplicates(n1)
    while o:
        print(o.val)
        o = o.next
