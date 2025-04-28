class Solution:
    def __init__(self):
        from collections import Counter
        
    def closeStrings(self, word1: str, word2: str) -> bool:
        Counter1 = Counter(word1)
        Counter2 = Counter(word2)
        
        hasSameCharacters = (Counter1.keys() == Counter2.keys())
        hasSameCountSets = (Counter(Counter1.values()) == Counter(Counter2.values()))
        if hasSameCharacters and hasSameCountSets:
            return True
        
        return False