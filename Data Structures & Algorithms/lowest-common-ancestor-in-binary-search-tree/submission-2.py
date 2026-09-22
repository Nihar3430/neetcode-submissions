# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root

        def dfs(node, p, q):
            if not node:
                return
            if node.val == p.val:
                self.res = p
            elif node.val == q.val:
                self.res = q
            elif p.val < node.val < q.val or p.val > node.val > q.val:
                self.res = node
            else:
                dfs(node.left, p, q)
                dfs(node.right, p, q)

        dfs(root, p, q)
        return self.res
            
