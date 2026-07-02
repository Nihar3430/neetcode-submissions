# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curK = 0
        self.result = None
        self.inorder(root, k)
        return self.result

    def inorder(self, node, k):
            if not node or self.result is not None:
                return
            self.inorder(node.left, k)

            self.curK+=1
            if self.curK == k:
                self.result = node.val
                self.curK += 1000
                return


            self.inorder(node.right, k)

    