# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr_k = 1
        self.res = None
        self.inorder(root, k)
        return self.result


    def inorder(self, root, k):
        if not root:
            return

        self.inorder(root.left, k)

        if self.curr_k == k:
            self.result = root.val
        self.curr_k += 1

        self.inorder(root.right, k)
