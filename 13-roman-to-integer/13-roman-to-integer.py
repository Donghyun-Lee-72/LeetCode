class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        num = 0             # total number added
        sub = 0             # if roman was subtraction, use 'sub' to subtract
        for char in s:    
            # if subtraction was started in last digit
            if sub != 0 and sub < roman[char] < sub*11:
                num = num - 2*sub
                sub = 0
            
            # if subtraction can be started
            if char in ["I", "X", "C"]:
                sub = roman[char]
            
            # add every value
            num += roman[char]
            
        return num