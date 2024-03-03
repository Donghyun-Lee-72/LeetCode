class Solution:
    def maxArea(self, height: List[int]) -> int:
        import numpy as np
        
        most_water = 0
        height = np.array(height)
        min_l_height = height[0]
        
        for l, l_height in enumerate(height[:-1]):
            if l_height < min_l_height:
                continue
            
            lower_bars = height[l+1:]*(np.arange(1, len(height)-l))
            higher_bars = (np.ones_like(height[l+1:])*l_height)*(np.arange(1, len(height)-l))
            r_heights = np.where(height[l+1:] < l_height, lower_bars, higher_bars)
            
            best_water = r_heights.max()
            if most_water < best_water:
                most_water = best_water
                min_l_height = l_height
        
        return most_water
    