class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        import numpy as np
        matrix = np.array(matrix)
        row_sum = np.sum(matrix, axis=1)
        col_sum = np.sum(matrix, axis=0)
        sum_n = (len(matrix)+1) * (len(matrix)//2) + (len(matrix)%2) * (len(matrix)//2+1)

        for i in range(len(matrix)):
            if len(np.unique(matrix[i,:])) != len(matrix):
                return False
            if len(np.unique(matrix[:,i])) != len(matrix):
                return False
        
        return np.all(row_sum==sum_n) and np.all(col_sum==sum_n)