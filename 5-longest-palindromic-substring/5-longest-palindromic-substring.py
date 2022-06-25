class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_rev = s[::-1]                             # reversed input string
        for length in range(len(s), 0, -1):         # from full length to 2
            last_start = len(s) - length + 1        # last starting idx at given length
            for start in range(0, last_start):      # idx of first element in substring
                half = int(round(length/2))         # half of length, rounded up
                end = len(s) - length - start       # rev_idx of last element in substring
                if s[start:start+half] == s_rev[end:end+half]:
                    substr = s[start:start+length]
                    return substr
                