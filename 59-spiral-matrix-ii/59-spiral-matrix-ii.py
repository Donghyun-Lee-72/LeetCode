class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0]*n for i in range(n)]
        i = 0
        next_stop = n
        x, y = 0, 0
        
        for cnt in range(1, n*n+1):
            arr[y][x] = cnt
            if cnt == next_stop:
                i += 1
                next_stop += n - (i+1)//2
                
            cnt += 1
            
            if i % 4 == 0:
                x += 1
            elif i % 4 == 1:
                y += 1
            elif i % 4 == 2:
                x -= 1
            else:
                y -= 1
                
        return arr