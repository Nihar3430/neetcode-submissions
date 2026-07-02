# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def dfs(self, p, q):
        if p and q:
            if not self.dfs(p.left, q.left):
                return False
                        
            if p.val != q.val:
                return False

            if not self.dfs(p.right, q.right):
                return False
            return True 


        if p and not q:
            return False

        if q and not p:
            return False
        return True 

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)

        