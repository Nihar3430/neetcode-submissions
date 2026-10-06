# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head

        prev = None
        curr = head
        after = head.next


        while after:
            curr.next = prev
            prev = curr
            curr = after
            after = after.next

        curr.next = prev


        return curr