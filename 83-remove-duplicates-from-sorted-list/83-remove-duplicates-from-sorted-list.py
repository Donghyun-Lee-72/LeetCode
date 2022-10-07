# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        last_node = ListNode(val=-101, next=head)
        
        if head == None:
            return head
        
        while head.next != None:
            if last_node.next.val == head.next.val:
                head = head.next
            else:
                last_node.next = head
                last_node = last_node.next
                head = head.next
                
        if last_node.next.val == head.val:
            last_node.next = head
        
        while start.next != None:
            if start.val == start.next.val:
                start = start.next
            else:
                break
        return start