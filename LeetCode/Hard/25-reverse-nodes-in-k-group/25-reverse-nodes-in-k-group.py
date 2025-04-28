# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        idx = 0
        vals = []
        nodes = []
        while head != None:
            vals.append(head.val)
            nodes.append(head)
            if idx % k == k - 1:
                for node, val in zip(nodes, vals[::-1]):
                    node.val = val
                nodes = []
                vals = []
            
            idx += 1
            head = head.next
            
        return start