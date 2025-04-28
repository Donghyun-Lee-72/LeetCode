# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, curr: Optional[TreeNode], targetSum: int, num: int, path: List[int], result: List[List[int]]) -> None:
        num += curr.val
        path = path + [curr.val]
        
        
        if curr.left == None and curr.right == None:
            if num == targetSum:
                result.append(path)
        if curr.left:
            self.helper(curr.left, targetSum, num, path, result)
        if curr.right:
            self.helper(curr.right, targetSum, num, path, result)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if root == None:
            pass
        else:
            self.helper(root, targetSum, 0, [], result)
        return result