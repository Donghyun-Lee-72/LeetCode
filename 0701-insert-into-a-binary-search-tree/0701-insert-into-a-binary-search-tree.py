# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, curr: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val < curr.val:
            if curr.left is None:
                return curr
            else:
                return self.find(curr.left, val)
        else:
            if curr.right is None:
                return curr
            else:
                return self.find(curr.right, val)
            
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        child = TreeNode(val=val)
        if root is None:
            return child
        parent = self.find(root, val)
        
        if val < parent.val:
            parent.left = child
        else:
            parent.right = child
        
        return root