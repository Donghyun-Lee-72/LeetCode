class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        import numpy as np
        n = len(nums)
        nums = np.array(nums)
        
        arr = np.zeros((n,n), dtype=int)
        arr = arr + nums
        arr = arr + nums.reshape(-1,1)
        
        mask = np.triu(np.ones(arr.shape, dtype=bool), k=1)
        selected_elements = arr[mask]
        cnt = np.sum(np.where(selected_elements<target,1,0))
        return cnt