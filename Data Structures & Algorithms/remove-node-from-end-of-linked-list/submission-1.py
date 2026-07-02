# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        temp = left

        while n > 1:
            right = right.next
            n -= 1

        while right.next:
            right = right.next
            temp = left
            left = left.next


        temp.next = left.next

        if left == head and left.next is None:
            head = None
        elif left == head:
            head = left.next

        return head