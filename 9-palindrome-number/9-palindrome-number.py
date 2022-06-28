class Solution:
    def isPalindrome(self, x: int) -> bool:
        from math import ceil
        
        if x < 0:
            return False
        
        arr = [int(a) for a in str(x)]
        half = int(ceil(len(arr)/2))
        if arr[:half] == arr[:-(half+1):-1]:
            return True
        else:
            return False