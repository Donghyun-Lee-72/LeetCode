class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        board = np.array(board)
        print(board)
        
        # check rows
        for i in range(9):
            row = board[i,:]
            arr = []
            for elem in row:
                if elem == ".":
                    continue
                else:
                    if elem in arr:
                        return False
                    else:
                        arr.append(elem)
            
        # check columns
        for j in range(9):
            col = board[:,j]
            arr = []
            for elem in col:
                if elem == ".":
                    continue
                else:
                    if elem in arr:
                        return False
                    else:
                        arr.append(elem)
            
        # check boxes
        for k in range(9):
            y,x = divmod(k, 3)
            box_x = 3*x
            box_y = 3*y
            flat = board[box_x:box_x+3,box_y:box_y+3].flatten()
            arr = []
            for elem in flat:
                if elem == ".":
                    continue
                else:
                    if elem in arr:
                        return False
                    else:
                        arr.append(elem)
        
        return True