# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = ListNode()                           # previous node of current node
        startNode = prevNode                            # one before first Node
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                currNode = ListNode(val=list1.val)      # current node
                prevNode.next = currNode
                prevNode = prevNode.next
                list1 = list1.next
            else:                                       # list1.val > list2.val
                currNode = ListNode(val=list2.val)
                prevNode.next = currNode
                prevNode = prevNode.next
                list2 = list2.next
        
        if list1 == None:
            prevNode.next = list2
        else:                                           # if list2.next == None
            prevNode.next = list1
        
        return startNode.next