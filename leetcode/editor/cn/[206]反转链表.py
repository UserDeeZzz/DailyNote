# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1217 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current_node, last_node = head, None
        while current_node:
            # 拆链
            next_code, current_node.next = current_node.next, last_node
            # 更新节点
            current_node, last_node = next_code, current_node
        return last_node

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    o = o.reverseList(n1)
    while o:
        print(o.val)
        o = o.next
