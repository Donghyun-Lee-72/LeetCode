class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        for char in s:
            try:
                t.remove(char)
            except:
                return False
        if len(t) == 0:
            return True
        else:
            return False