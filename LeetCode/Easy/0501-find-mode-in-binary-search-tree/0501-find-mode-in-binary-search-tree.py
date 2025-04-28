# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        cnt = dict()
        queue = [root]

        while len(queue) > 0:
            cur_node = queue.pop(0)
            cnt[cur_node.val] = cnt.get(cur_node.val, 0) + 1

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)
        
        max_val = max(cnt.values())
        max_arr = [key for key, val in cnt.items() if val == max_val]
        return max_arr