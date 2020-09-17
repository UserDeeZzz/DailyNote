# 给定一个二叉树，返回它的 前序 遍历。 
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
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 367 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if root is None: return ans
    #     ans.append(root.val)
    #     ans.extend(self.preorderTraversal(root.left))
    #     ans.extend(self.preorderTraversal(root.right))
    #     return ans
    # bb递归
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if root is None: return ans
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         ans.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return ans
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            res = stack.pop()
            if isinstance(res,TreeNode):
                stack.extend([res.right, res.left, res.val])
            elif isinstance(res,int):
                ans.append(res)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
