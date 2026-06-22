# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        start = None
        if list1.val > list2.val:
            start = list2
            list2 = list2.next
        else:
            start = list1
            list1 = list1.next
        
        current = start
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        if list2 is not None:
            current.next = list2
        if list1 is not None:
            current.next = list1

        return start