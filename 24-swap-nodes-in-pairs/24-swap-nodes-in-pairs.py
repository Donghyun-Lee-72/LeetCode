# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper_swapPairs(self, prev: Optional[ListNode]) -> None:
        """
        Swaps next pair (next node, next next node)
        prev: previous node of the pair
        return: last node in pair
        """
        head = prev.next
        if head == None or head.next == None:
            return
        
        after = head.next.next
        prev.next = head.next
        prev.next.next = head
        head.next = after
        self.helper_swapPairs(head)
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        pre_start = ListNode
        pre_start.next = head
        self.helper_swapPairs(pre_start)
        return pre_start.next