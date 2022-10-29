# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        original_stack = [original]
        cloned_stack = [cloned]
        
        while original_stack:
            curr = original_stack.pop(0)
            result = cloned_stack.pop(0)
            
            if curr is target:
                break
            
            if curr.left is not None:
                original_stack.append(curr.left)
                cloned_stack.append(result.left)
            if curr.right is not None:
                original_stack.append(curr.right)
                cloned_stack.append(result.right)
        
        return result