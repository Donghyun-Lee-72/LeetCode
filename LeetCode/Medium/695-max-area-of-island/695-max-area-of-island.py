class Solution:
    def helper(self, isVisited: List[List[bool]], grid: List[List[int]], loc: List[int], mn: List[int], size: int=0) -> int:
        if isVisited[loc[0]][loc[1]]:
            return size
        if grid[loc[0]][loc[1]] == 0:
            return size
        
        isVisited[loc[0]][loc[1]] = True
        size += 1
        
        if loc[0] > 0:
            loc1 = [loc[0]-1, loc[1]]
            size = self.helper(isVisited, grid, loc1, mn, size)
        if loc[1] > 0:
            loc2 = [loc[0], loc[1]-1]
            size = self.helper(isVisited, grid, loc2, mn, size)
        if loc[0] < mn[0]-1:
            loc3 = [loc[0]+1, loc[1]]
            size = self.helper(isVisited, grid, loc3, mn, size)
        if loc[1] < mn[1]-1:
            loc4 = [loc[0], loc[1]+1]
            size = self.helper(isVisited, grid, loc4, mn, size)
        
        return size
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        matrix_size = [m, n]
        isVisited = [ [ False for i in range(n) ] for j in range(m) ]
        area = 0
        
        for i in range(m*n):
            loc = [i//n, i%n]
            area = max(area, self.helper(isVisited, grid, loc, matrix_size, size=0))
        
        return area
        