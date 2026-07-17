# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.rootcopy = root

        if root is None:
            root = TreeNode(val, None, None)
            return root

        while True:
            if val < root.val and root.left:
                root = root.left
            elif val < root.val and not root.left:
                root.left = TreeNode(val, None, None)
                break
            elif val > root.val and root.right:
                root = root.right
            elif val > root.val and not root.right:
                root.right = TreeNode(val, None, None)
                break

        return self.rootcopy