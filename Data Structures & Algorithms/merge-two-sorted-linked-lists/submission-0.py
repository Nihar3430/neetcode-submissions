# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        pointer1 = list1
        pointer2 = list2
        newList = ListNode()
        headToReturn = newList

        while pointer1 is not None and pointer2 is not None:
            if pointer1.val < pointer2.val:
                newList.next = pointer1
                pointer1 = pointer1.next
                newList = newList.next
            else:
                newList.next = pointer2
                pointer2 = pointer2.next
                newList = newList.next
            
        if pointer1 is not None:
            newList.next = pointer1

        if pointer2 is not None:
            newList.next = pointer2
        return headToReturn.next

        