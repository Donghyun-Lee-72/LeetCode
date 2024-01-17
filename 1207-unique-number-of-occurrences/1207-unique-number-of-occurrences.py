class Solution:
    def __init__(self):
        from collections import Counter
        
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(Counter(arr).values()) == len(set(Counter(arr).values())): return True
        else: return False