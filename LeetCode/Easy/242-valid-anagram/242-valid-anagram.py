class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars_from = list(s)
        chars_to = list(t)
        for char in chars_to:
            idx = s.find(char)
            if idx == -1:
                return False
            else:
                s = s[:idx] + s[(idx+1):]
        return True