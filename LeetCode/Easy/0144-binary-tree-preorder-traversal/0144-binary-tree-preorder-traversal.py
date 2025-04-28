# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, result: List[TreeNode], node: Optional[TreeNode]) -> None:
        if node == None:
            return
        else:
            result.append(node.val)
            
        self.helper(result, node.left)
        self.helper(result, node.right)
        return
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(result, root)
        return result