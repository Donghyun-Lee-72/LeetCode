class Solution:
    def isPalindrome(self, s: str) -> bool:
        # https://www.techiedelight.com/remove-non-alphanumeric-characters-string-python/
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False