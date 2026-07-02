from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        cols = len(grid[0])
        rows = len(grid)

        self.num_islands = 0


        def bfs(i, j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))
            moves = [[0,1], [1,0], [0,-1], [-1,0]]
            self.num_islands += 1

            while q:
                cr, cc = q.popleft()

                for move in moves:
                    mR = cr + move[0]
                    mC = cc + move[1]

                    if mR in range(rows) and mC in range(cols) and grid[mR][mC] == "1" and (mR, mC) not in visited:
                        q.append((mR, mC))
                        visited.add((mR, mC))

                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        bfs(i, j)
        
        return self.num_islands
                


        


