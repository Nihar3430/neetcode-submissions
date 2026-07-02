# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node: Optional[TreeNode], subnode: Optional[TreeNode]) -> bool:
        if node is None and subnode is None:
            return True
        if node is None or subnode is None:
            return False
        if node.val != subnode.val:
            return False
        return self.dfs(node.left, subnode.left) and self.dfs(node.right, subnode.right)

    # Scan the big tree for any node whose subtree matches subRoot
    def find_node(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        # If values match, check full subtree equality
        if root.val == subRoot.val and self.dfs(root, subRoot):
            return True
        # Otherwise, keep searching
        return self.find_node(root.left, subRoot) or self.find_node(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        return self.find_node(root, subRoot)