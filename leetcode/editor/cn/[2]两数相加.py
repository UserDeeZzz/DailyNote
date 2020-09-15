# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 4886 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = tail = ListNode(-1)

        v = 0
        while l1 or l2:
            if l1 is None:
                l1_s = 0
            else:
                l1_s = l1.val
                l1 = l1.next
            if l2 is None:
                l2_s = 0
            else:
                l2_s = l2.val
                l2 = l2.next
            v, c = divmod(l1_s + l2_s + v, 10)
            tail.next = ListNode(c)
            tail = tail.next
        if v != 0:
            tail.next = ListNode(v)
        return res.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3

    k1 = ListNode(5)
    k2 = ListNode(6)
    k3 = ListNode(4)

    k1.next = k2
    k2.next = k3

    o = o.addTwoNumbers(n1, k1)
    while o:
        print(o.val)
        o = o.next
