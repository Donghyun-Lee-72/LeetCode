class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = None
        res = 0
        for char in s:
            if prev is None:
                prev = ord(char)
            else:
                curr = ord(char)
                res += abs(curr-prev)
                prev = curr
        return res