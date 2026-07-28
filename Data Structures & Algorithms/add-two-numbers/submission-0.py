# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumNode = ListNode()
        res = sumNode

        self.carry = 0

        while l1 or l2 or self.carry > 0:
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val

            curSum = 0

            curSum = v1 + v2 + self.carry

            modulo = curSum % 10
            self.carry = curSum // 10

            sumNode.next = ListNode(modulo)
            sumNode = sumNode.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return res.next


