class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x < 0:
            num = -1*int(x_str[:0:-1])
        else:
            num = int(x_str[::-1])
        
        if -2**31 < num < 2**31 - 1:
            return num
        else:
            return 0