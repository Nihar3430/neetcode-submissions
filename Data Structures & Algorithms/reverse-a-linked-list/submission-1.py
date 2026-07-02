# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        if head.next is None:
            return head
        
        if head.next.next is None:
            second = head.next
            second.next = head
            head.next = None
            return second

        curr, prev, after = head.next, head, head.next.next

        while after is not None:
            curr.next = prev
            prev = curr
            curr = after
            after = curr.next

        curr.next = prev

        head.next = None


        return curr
        