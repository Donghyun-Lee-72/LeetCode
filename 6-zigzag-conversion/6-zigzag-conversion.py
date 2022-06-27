class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                        # if numRows == 1
            return s
        
        matrix = [ [] for _ in range(numRows) ]
        idx = 0
        for i, char in enumerate(s):
            matrix[idx].append(char)
            print(i, char, idx)
            
            # modify idx
            if numRows == 2:                    # if numRows == 2
                idx = (i+1) % 2
            else:
                x = i // (numRows-1)                # number of corner of zigzags gone
                if x % 2 == 0 :                     # if going down
                    idx += 1
                else:                               # if going up
                    idx -= 1
        
        print(matrix)
        result = ""
        for y in range(numRows):
            string = "".join(matrix[y])
            result += string
        return result
           