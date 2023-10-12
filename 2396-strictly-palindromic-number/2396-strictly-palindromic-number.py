class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        import math
        
        if n % 2 == 0:
            return False
        
        for i in range(2, n-1):
            highest_deg = math.floor(math.log(n, i))
            num = n
            for j in range(0, highest_deg+1):
                num -= i**j + i**(highest_deg-j)
                if num < 0:
                    return False
                elif num == 0:
                    break
        return True