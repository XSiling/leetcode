class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        grid_n = len(grid)
        result_grid = [[0 for j in range(grid_n -2)] for i in range(grid_n-2)]
        for i in range(len(result_grid)):
            for j in range(len(result_grid)):
                #(i+1, j+1)
                current_max = -1
                for kk in range(-1,2):
                    for tt in range(-1,2):
                        if grid[i+1+kk][j+1+tt] > current_max:
                            current_max = grid[i+1+kk][j+1+tt]
                result_grid[i][j] = current_max
        
        return result_grid

