# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        bad_node = head
        node = head

        for i in range(n):
            bad_node = bad_node.next

        if bad_node is None:
            return head.next

        while bad_node.next:
            node = node.next
            bad_node = bad_node.next

        node.next = node.next.next
        

        return head

        