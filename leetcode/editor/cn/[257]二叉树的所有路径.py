# 给定一个二叉树，返回所有从根节点到叶子节点的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  输入:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3 
#  Related Topics 树 深度优先搜索 
#  👍 383 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []

        def dfs(node, path):
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            elif not node.left:
                dfs(node.right, path + '->')
            elif not node.right:
                dfs(node.left, path + '->')
            else:
                dfs(node.right, path + '->')
                dfs(node.left, path + '->')

        dfs(root, '')
        return res

# leetcode submit region end(Prohibit modification and deletion)
