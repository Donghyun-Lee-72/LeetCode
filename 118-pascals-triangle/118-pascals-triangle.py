class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [ [ 1 for _ in range(i) ] for i in range(1, numRows+1) ]
        for i in range(len(triangle)):
            row = triangle[i]
            if len(row) < 3:
                continue
            else:
                for j in range(1,len(row)-1):
                    pre_row = triangle[i-1]
                    row[j] = pre_row[j-1] + pre_row[j]
        return triangle