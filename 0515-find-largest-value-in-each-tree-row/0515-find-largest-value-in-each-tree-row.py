# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return None
        
        row_cnt = 0
        missing_cnt = 0
        next_row_missing_cnt = 0
        depth = 0
        row_vals = []
        max_vals = []
        
        queue = [root]
        
        while(len(queue) > 0):
            node = queue.pop(0)
            row_cnt += 1
            row_vals.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            else:
                next_row_missing_cnt += 1 
                
            if node.right is not None:
                queue.append(node.right)
            else:
                next_row_missing_cnt += 1
                
            if row_cnt + missing_cnt >= 2**depth:
                max_vals.append(max(row_vals))
                row_vals = []
                row_cnt = 0
                missing_cnt = missing_cnt*2 + next_row_missing_cnt
                next_row_missing_cnt = 0
                depth += 1
    
        if row_vals:
            max_vals.append(max(row_vals))
    
        return max_vals