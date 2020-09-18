# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 394 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if root is None:return []
    #     ans.extend(self.postorderTraversal(root.left))
    #     ans.extend(self.postorderTraversal(root.right))
    #     ans.append(root.val)
    #     return ans
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root is not None:
                stack.append(root)
                ans.append(root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return ans[::-1]


    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if isinstance(node, TreeNode):
    #             stack.extend([node.val, node.right, node.left])
    #         elif isinstance(node, int):
    #             ans.append(node)
    #     return ans

# leetcode submit region end(Prohibit modification and deletion)
