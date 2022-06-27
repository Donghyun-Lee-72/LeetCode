class Solution:
    def longestPalindrome(self, s: str) -> str:
        # copied from https://sub2n.github.io/2019/04/22/LeetCode-5-Longest-Palindromic-Substring/
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
        return s[i: i+l]