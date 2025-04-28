class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = str(bin(x))[2:]
        bin_y = str(bin(y))[2:]
        cnt = 0
        short = min(len(bin_x), len(bin_y))
        
        for i in range(short):
            i += 1
            if bin_x[-i] != bin_y[-i]:
               cnt += 1
        
        if len(bin_x) < len(bin_y):
            for j in range(len(bin_y)-short):
                if bin_y[j] == "1":
                    cnt += 1
                
        elif len(bin_y) < len(bin_x):
            for k in range(len(bin_x)-short):
                if bin_x[k] == "1":
                    cnt += 1
        
        return cnt