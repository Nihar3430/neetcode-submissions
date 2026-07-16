# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.summ = 0

        def dfs(root, num):
            num *= 10
            num += root.val
            
            if not root.left and not root.right:
                self.summ += num

            if root.left:
                dfs(root.left, num)

            if root.right:
                dfs(root.right, num)
            


        dfs(root, 0)
        return self.summ

