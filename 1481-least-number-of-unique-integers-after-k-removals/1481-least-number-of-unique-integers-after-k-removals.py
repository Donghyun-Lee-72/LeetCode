class Solution:
    def __init__(self):
        from collections import Counter
    
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        occurrence_sorted = sorted(Counter(arr).values())
        for i, occur in enumerate(occurrence_sorted):
            k -= occur
            if k == 0:
                return len(occurrence_sorted) - (i+1)
            elif k < 0:
                return len(occurrence_sorted) - (i+1) + 1
        return 1
        
        