class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = { 1: "I", 4: "IV", 5: "V", 9: "IX",
                      10: "X", 40: "XL", 50: "L", 90: "XC",
                      100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }
        integer = sorted(dictionary.keys(), reverse=True)
        result = ""
        
        for key in integer:
            div = num // key
            num -= key*div
            result += dictionary[key]*div
        
        return result
            