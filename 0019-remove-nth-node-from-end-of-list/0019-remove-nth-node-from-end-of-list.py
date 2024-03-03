# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_dict = dict()
        cnt = 0
        while head:
            nodes_dict[cnt] = head
            
            head = head.next
            cnt += 1
        
        idx = cnt - n
        if idx == 0:
            return None if len(nodes_dict) == 1 else nodes_dict[1]
        else:
            nodes_dict[idx-1].next = nodes_dict[idx].next
            return nodes_dict[0]