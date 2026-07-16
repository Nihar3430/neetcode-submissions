# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxx):
            if root.val >= maxx:
                self.res = self.res + 1
                maxx = root.val

            if root.left:
                dfs(root.left, maxx)
            if root.right:
                dfs(root.right, maxx)


        self.res = 0
        dfs(root, root.val)

        return self.res
             

