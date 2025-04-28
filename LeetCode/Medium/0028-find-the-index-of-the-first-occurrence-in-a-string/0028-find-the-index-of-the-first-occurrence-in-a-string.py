class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_hay = len(haystack)
        len_nee = len(needle)
        for start in range(0, len_hay - len_nee + 1):
            if haystack[start:start+len_nee] == needle:
                return start
        return -1
        