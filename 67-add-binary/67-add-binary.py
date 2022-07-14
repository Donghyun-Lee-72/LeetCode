class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_str = "0b"
        sum_num = bin(int(bin_str+a, 2) + int(bin_str+b, 2))
        return sum_num[2:]
        
            