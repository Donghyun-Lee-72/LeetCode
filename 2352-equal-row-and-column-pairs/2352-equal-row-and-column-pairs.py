class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid)
        for i in range(n):
            col = [ grid[j][i] for j in range(n) ]
            cnt += grid.count(col)
        return cnt