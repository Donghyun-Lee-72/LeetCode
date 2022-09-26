class Solution:
    def trap(self, height: List[int]) -> int:
        import numpy as np
        
        if len(height) < 3:
            return 0
        
        total = 0
        sorted_idx = np.argsort(height)[::-1]
        start = sorted_idx[0]
        right_end = left_end = start
        
        for idx in sorted_idx[1:]:
            if height[idx] == 0:
                break
            
            if idx < left_end:
                for i in range(idx+1, left_end):
                    total += height[idx]-height[i]
                left_end = idx
            elif right_end < idx:
                for i in range(right_end+1, idx):
                    total += height[idx]-height[i]
                right_end = idx
            else:
                continue
    
        return total
                