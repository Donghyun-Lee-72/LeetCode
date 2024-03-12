# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes, cum_sum = [], []
        curr = head
        
        while curr:
            nodes.append(curr)
            cum_sum = [val+curr.val for val in cum_sum]
            cum_sum.append(curr.val)
            
            try:
                idx_zero = cum_sum.index(0)
                
                if idx_zero == 0:
                    head = curr.next
                    nodes, cum_sum = [], []
                else:
                    nodes[idx_zero-1].next = curr.next
                    nodes = nodes[:idx_zero]
                    cum_sum = cum_sum[:idx_zero]
            except ValueError:
                pass
            
            curr = curr.next
        
        return head