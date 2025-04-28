class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2, 0, -1):
            q, r = divmod(len(s), i)
            if r == 0:
                substr = [ s[j:j+i] for j in range(0, len(s), i) ]
                if not substr or [substr[0]]*len(substr) == substr:
                    return True
        
        return False