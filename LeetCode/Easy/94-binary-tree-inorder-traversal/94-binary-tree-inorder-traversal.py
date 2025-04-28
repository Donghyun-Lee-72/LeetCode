# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, curr: Optional[TreeNode], traversal: List[int]):
        if curr == None:
            return
        
        self.helper(curr.left, traversal)
        traversal.append(curr.val)
        self.helper(curr.right, traversal)
        return
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.helper(root, traversal)
        return traversal
        