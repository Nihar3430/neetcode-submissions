# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if node.left:
                resl = dfs(node.left)
                if resl:
                    node.left = None

            if node.right:
                resr = dfs(node.right)
                if resr:
                    node.right = None

            if node.val == target and not node.left and not node.right:
                return True
            else:
                return False

        dfs(root)

        if root.val == target and not root.left and not root.right:
                root = None

        return root