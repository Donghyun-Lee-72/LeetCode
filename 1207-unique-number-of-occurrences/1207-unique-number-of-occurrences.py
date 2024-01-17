class Solution:
    def __init__(self):
        from collections import Counter
        
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr).values()
        if len(occurences) == len(set(occurences)): return True
        else: return False