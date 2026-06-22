# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast and fast.next and fast.next.next:
            if slow == fast:
                print(slow.val, fast.val)
                return True
            slow = slow.next
            fast = fast.next
            if slow == fast:
                print(slow.val, fast.val)
                return True
            fast = fast.next
            if slow == fast:
                return True
        return False