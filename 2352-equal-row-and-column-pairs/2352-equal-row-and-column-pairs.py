class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid)
        # for i in range(n):
            # col = [ grid[j][i] for j in range(n) ]
        for col in zip(*grid):
            cnt += grid.count(list(col))
        return cnt