class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        
        counter1 = Counter(arr1)
        res = []
        for elem in arr2:
            res.extend([elem] * counter1[elem])
            del counter1[elem]
        
        if counter1:
            keys = sorted(counter1.keys())
            for key in keys:
                res.extend([key]*counter1[key])
        
        return res