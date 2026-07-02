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

        q = deque([(root, 0)])


        ans = []
        temp_ans = []
        current_level = 0

        while q:
            node, level = q.popleft()

            if node.left is not None:
                q.append((node.left, level + 1))

            if node.right is not None:    
                q.append((node.right, level + 1))

            if level == current_level:
                temp_ans.append(node.val)
            else:
                ans.append(temp_ans)
                temp_ans = []
                current_level = level
                temp_ans.append(node.val)

        ans.append(temp_ans)
        return ans


