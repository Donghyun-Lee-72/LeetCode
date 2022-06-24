class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        num = 0
        idx = 0
        
        if len(s) == 0:
            return 0
        
        if ord(s[0]) == 45:
            sign = -1
            idx += 1
        elif ord(s[0]) == 43:
            sign = 1
            idx += 1
        
        while idx < len(s) and 48 <= ord(s[idx]) <= 57:
            num = 10*num + int(s[idx])
            idx += 1    
        
        num = sign * num
        if num < -1*2**31:
            return -1*2**31
        elif 2**31 - 1 < num:
            return 2**31 - 1
        else:
            return num