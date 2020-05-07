class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid==[]: return 0
        M, N = len(grid), len(grid[0])
        for j in range(N):
            for i in range(M):
                if (i-1) >= 0 and (j-1) >=0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif (i-1) >= 0:
                    grid[i][j] += grid[i-1][j]
                elif (j-1) >= 0:
                    grid[i][j] += grid[i][j-1]
        return grid[M-1][N-1]