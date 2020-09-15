# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。 
# 
#  你应当保留两个分区中每个节点的初始相对位置。 
# 
#  示例: 
# 
#  输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#  
#  Related Topics 链表 双指针 
#  👍 252 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, cur, last = None, head, None
        while cur:
            # 向左半区移动
            if cur.val < x:
                # 刚开始遍历 cur = head
                if last is None:
                    left = cur
                    # 移动cur
                    cur, last = cur.next, cur
                else:
                    # 左半区为空
                    if left is None:
                        cur_next = cur.next  # 下一个结点
                        last.next = cur_next  # 上一个结点连接下一个结点
                        cur.next = head  # 结点作为头
                        head = cur  # 作为头结点
                    else:
                        left_next, cur_next = left.next, cur.next # cur None
                        # 右半区不为空
                        if left_next != cur:
                            last.next = cur_next  # None
                            left.next = cur
                            cur.next = left_next

                    left = cur
                    cur = cur_next # None
            else:
                cur, last = cur.next, cur
        return head
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    o = Solution()
    n1 = ListNode(1)
    n2 = ListNode(1)
    # n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    o = o.partition(n1, 2)
    while o:
        print(o.val)
        o = o.next