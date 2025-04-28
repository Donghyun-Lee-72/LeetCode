class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        import numpy as np
        
        satisfaction_sorted = np.sort(satisfaction)
        for i in range(len(satisfaction)):
            sum = np.sum(satisfaction_sorted[i:])
            if 0 < sum:
                break
        
        coef = np.sum(satisfaction_sorted[i:]*np.arange(1,len(satisfaction_sorted)+1-i))
        return max(0, coef)