# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#  
# 
#  说明： 
# 
#  给定的 n 保证是有效的。 
# 
#  进阶： 
# 
#  你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针 
#  👍 991 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 因为没有上一个结点 所以交换值 并删除下一个结点
        node.val = node.next.val
        node.next = node.next.next

# leetcode submit region end(Prohibit modification and deletion)
