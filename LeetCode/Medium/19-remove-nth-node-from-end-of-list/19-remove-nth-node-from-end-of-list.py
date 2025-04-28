# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        prev = head
        
        for _ in range(n):
            head = head.next
        if head == None:
            return start.next
        head = head.next
        
        while head != None:
            head = head.next
            prev = prev.next
        
        prev.next = prev.next.next
        return start