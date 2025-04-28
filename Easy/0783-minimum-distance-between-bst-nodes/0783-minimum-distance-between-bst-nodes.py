# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        import numpy as np
        
        stack = [root]
        numbers = []
        
        while stack:
            curr = stack.pop(0)
            numbers.append(curr.val)
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        
        numbers.sort()
        diff = numbers[-1]
        for i, j in zip(numbers[:-1], numbers[1:]):
            if j - i < diff:
                diff = j - i
                
        return diff