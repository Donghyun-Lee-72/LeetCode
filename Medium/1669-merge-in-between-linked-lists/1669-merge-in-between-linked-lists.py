# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cnt = 1
        curr_a = list1
        while cnt < a:
            curr_a = curr_a.next
            cnt += 1
        curr_b = curr_a.next
        curr_a.next = list2
        while cnt <= b:
            curr_b = curr_b.next
            cnt += 1
        while curr_a.next:
            curr_a = curr_a.next
        curr_a.next = curr_b
        return list1