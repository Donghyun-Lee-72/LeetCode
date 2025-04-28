# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(a, b):
        """
        Euclidean algorithm to find GCD.
        Learned and referenced from Geeks for geeks. Thank you.
        https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
        """
        if a == 0:
            return b

        return gcd(b % a, a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        next = head.next
        
        if next == None:
            return head
        
        while next:
            gcd_val = gcd(curr.val, next.val)
            curr.next = ListNode(gcd_val, next)
            curr = next
            next = next.next
        
        return head