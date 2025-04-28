# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfsSearch(self, root: Optional[TreeNode], currPath: List[TreeNode], allPath: List[TreeNode]) -> None:
        if root is None:
            return
        elif root.left is None and root.right is None:
            pathNow = currPath + [str(root.val)]
            allPath.append("->".join(pathNow))
            return
        
        pathNow = currPath + [str(root.val)]
        self.dfsSearch(root.left, pathNow, allPath)
        self.dfsSearch(root.right, pathNow, allPath)
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.dfsSearch(root, [], paths)
        return paths