class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        import numpy as np
        hours = np.array(hours)
        cnt = np.sum(np.where(hours>=target,1,0))
        return cnt