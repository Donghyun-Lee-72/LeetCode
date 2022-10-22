# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swapNodes(self, nodes: List[Optional[TreeNode]]):
        vals = [ node.val for node in nodes ]
        for node, val in zip(nodes, vals[::-1]):
            node.val = val

        return
    
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        import math
        cnt = 0
        stack = [root]
        
        while stack:
            cnt += 1
            
            if math.log2(cnt) % 2 == 1:
                level = math.floor(math.log2(cnt))
                self.swapNodes(stack[:2**level])
                
            curr = stack.pop(0)
            
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
                
        return root
            