# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root: Optional[TreeNode], depth: int, sums: Dict[int, int]) -> None:
        if root is None:
            return
        
        sums[depth] = sums.get(depth, 0) + root.val
        
        if root.left:
            self.bfs(root.left, depth+1, sums)
        if root.right:
            self.bfs(root.right, depth+1, sums)
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = { 1:0 }
        self.bfs(root, 1, sums)
        max_key = max(sums, key=sums.get)
        
        return max_key