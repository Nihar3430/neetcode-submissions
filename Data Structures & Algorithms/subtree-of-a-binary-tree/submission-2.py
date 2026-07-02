# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, subnode):
        if node is None and subnode is None:
            return True
        if node is None or subnode is None:
            return False
        if node.val != subnode.val:
            return False
        return self.dfs(node.left, subnode.left) and self.dfs(node.right, subnode.right)
        
    def find_node(self, root, subRoot):
        if root is None:
            return False

        # if values match, check the entire subtree
        if root.val == subRoot.val and self.dfs(root, subRoot):
            return True

        # IMPORTANT: return the recursive results, don’t discard them
        return self.find_node(root.left, subRoot) or self.find_node(root.right, subRoot)



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.find_node(root, subRoot)

