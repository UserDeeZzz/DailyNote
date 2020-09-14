# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 
#  👍 510 👎 0

from copy import copy
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None
        idx = 1
        cur1, last1 = head, None
        while idx < m:
            cur1, last1 = cur1.next, cur1  # 2 1
            idx += 1
        # last1 -- 断 -- cur1
        # last2 -- 断 -- cur2
        cur2, last2 = cur1, None
        while idx <= n:
            next_code, cur2.next = cur2.next, last2
            cur2, last2 = next_code, cur2 # 5,4
            idx += 1
        # cur1连cur2 如果翻转部分长度为0 那么不连接
        if last2 is not None:
            cur1.next = cur2
        # last1连last2
        if last1 is not None:
            last1.next = last2
        # 第一部分未翻转的长度为0 那么直接从第二部分开始
        else:
            return last2

        return head


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    # n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    o = o.reverseBetween(n1, 1, 2)
    while o:
        print(o.val)
        o = o.next




