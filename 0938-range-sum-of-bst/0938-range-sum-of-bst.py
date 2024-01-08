# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = [0]
        self.rangeSumBSTHelper(root, low, high, result)
        return result[0]
    
    def rangeSumBSTHelper(self, curr: Optional[TreeNode], low: int, high: int, sumNum: List[int]) -> None:
        if curr is None:
            return
        
        if low <= curr.val <= high:
            sumNum[0] = sumNum[0] + curr.val
        
        if low <= curr.val:
            self.rangeSumBSTHelper(curr.left, low, high, sumNum)
        if curr.val <= high:
            self.rangeSumBSTHelper(curr.right, low, high, sumNum)
        return