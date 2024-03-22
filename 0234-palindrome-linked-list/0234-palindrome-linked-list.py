# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        from collections import deque
        
        list_deque = deque()
        while head:
            list_deque.append(head.val)
            head = head.next
        
        while len(list_deque) > 1:
            if list_deque.popleft() != list_deque.pop():
                return False
        
        return True