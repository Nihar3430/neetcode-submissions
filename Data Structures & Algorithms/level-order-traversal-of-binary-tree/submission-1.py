# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        temp = []
        level = 0

        q = deque([(root, 0)])

        while len(q) != 0:
            root, l = q.popleft()

            if root.left:
                q.append((root.left, l + 1))
            
            if root.right:
                q.append((root.right, l + 1))

            if l == level:
                temp.append(root.val)
            else:
                level = l
                result.append(temp)
                temp = []
                temp.append(root.val)

        result.append(temp)

        return result

            