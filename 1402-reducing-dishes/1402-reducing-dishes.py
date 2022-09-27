class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        import numpy as np
        
        satisfaction_sorted = np.sort(satisfaction)
        multiplier = np.arange(1,len(satisfaction)+1)
        coef = np.sum(satisfaction_sorted * multiplier)
        
        for i in range(len(satisfaction)):
            sum = np.sum(satisfaction_sorted[i:])
            if 0 < sum:
                return coef
            else:
                coef -= sum
        return coef