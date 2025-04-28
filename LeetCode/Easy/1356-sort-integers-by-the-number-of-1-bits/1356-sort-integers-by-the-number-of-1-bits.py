class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        import numpy as np
        
        arr = sorted(arr)
        arr_bin_cnt = [ bin(num)[2:].count('1') for num in arr ]
        mask = np.argsort(arr_bin_cnt, kind='stable')
        return [arr[i] for i in mask]