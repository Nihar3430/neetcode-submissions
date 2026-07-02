# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        temp = None
        curr = mid

        while curr:
            future = curr.next
            curr.next = temp
            temp = curr
            curr = future

        l = head
        r = temp



        while r:
            lnext = l.next
            rnext = r.next
            l.next = r
            r.next = lnext
            l = r.next
            r = rnext



