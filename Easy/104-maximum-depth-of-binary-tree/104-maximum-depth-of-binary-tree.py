# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, head: Optional[TreeNode], depth: int) -> int:
        if head == None:
            return depth
        
        depth += 1
        depth_left = self.helper(head.left, depth)
        depth_right = self.helper(head.right, depth)
        return max(depth_left, depth_right)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.helper(root, 0)
        return depth