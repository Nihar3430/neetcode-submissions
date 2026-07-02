# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        prev = None
        curr = mid

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after

        l = head
        r = prev

        while r:
            l_next = l.next
            r_next = r.next
            l.next = r
            r.next = l_next
            l = r.next
            r = r_next







