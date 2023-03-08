class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxResultGrid = [[0 for i in range(n)] for j in range(m)]
        maxResultGrid[0][0] = grid[0][0]
        for i in range(1, m):
            maxResultGrid[i][0] = maxResultGrid[i-1][0] + grid[i][0]
        for i in range(1, n):
            maxResultGrid[0][i] = maxResultGrid[0][i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                maxResultGrid[i][j] = max(maxResultGrid[i-1][j], maxResultGrid[i][j-1]) + grid[i][j]
        
        return maxResultGrid[m-1][n-1]
