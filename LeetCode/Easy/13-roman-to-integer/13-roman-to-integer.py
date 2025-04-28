class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        roman_set = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD":400, "CM":900 }
        num = 0             # total number added
        i = 0
        while i < len(s):
            if s[i:i+2] in roman_set:
                num += roman_set[s[i:i+2]]
                i += 2
            else:
                num += roman[s[i]]
                i += 1
                
        return num