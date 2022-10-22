# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        cnt = 0
        stack = [root]
        while stack:
            curr = stack.pop(0)
            cnt += 1
                
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)

        return cnt
        
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        stack = [root]
        while stack:
            curr = stack.pop(0)
            
            if curr.val == x:
                cnt_left = self.bfs(curr.left)
                cnt_right = self.bfs(curr.right)
                break
                
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
                
        half = n / 2
        if cnt_left > half:
            return True
        elif cnt_right > half:
            return True
        elif (cnt_left + cnt_right + 1) < half:
            return True
        else:
            return False