# 给定一个二叉树，原地将它展开为一个单链表。 
# 
#  
# 
#  例如，给定二叉树 
# 
#      1
#    / \
#   2   5
#  / \   \
# 3   4   6 
# 
#  将其展开为： 
# 
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6 
#  Related Topics 树 深度优先搜索 
#  👍 585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        r = root.right
        l = root.left
        root.left = None
        root.right = l
        while root.right:
            root = root.right
        root.right = r



# leetcode submit region end(Prohibit modification and deletion)
