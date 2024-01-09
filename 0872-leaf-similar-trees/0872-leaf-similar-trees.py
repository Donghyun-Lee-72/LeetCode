# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafSeq1 = []
        leafSeq2 = []
        
        self.getLeafSeq(root1, leafSeq1)
        self.getLeafSeq(root2, leafSeq2)
        
        if leafSeq1 == leafSeq2:
            return True
        else:
            return False
        
    def getLeafSeq(self, curr: Optional[TreeNode], seq: List[int]) -> None:
        if curr is None:
            return
        
        if curr.left is None and curr.right is None:
            seq.append(curr.val)
            return
        
        self.getLeafSeq(curr.left, seq)
        self.getLeafSeq(curr.right, seq)