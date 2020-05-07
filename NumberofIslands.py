class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: #BFS Solution
        if grid==[] or grid[0]==[]: return 0
        M = len(grid)
        N = len(grid[0])
        q = deque() # [] works too
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inside = lambda x,y: 0<=x and x<M and 0<=y and y<N 
        answer = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':
                    grid[i][j] = 2 # two for visited
                    answer+=1
                    q.append((i,j))
                    while q:
                        fr = q.popleft() # pop
                        for di in directions:
                            new_row = fr[0] + di[0]
                            new_col = fr[1] + di[1]
                            if inside(new_row, new_col) and grid[new_row][new_col] == '1':
                                grid[new_row][new_col]=2
                                q.append((new_row, new_col))
        return answer