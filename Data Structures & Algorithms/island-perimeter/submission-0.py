from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        self.perimeter = 0

        self.i = 0
        self.j = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.i = r
                    self.j = c


        q.append((self.i,self.j))
        grid[self.i][self.j] = -1

        while q:
            row,col = q.popleft()
            count = 0
            if row-1 >= 0:
                if grid[row-1][col] == 1:
                    grid[row-1][col] = -1
                    count += 1
                    q.append((row-1,col))
                elif grid[row - 1][col] == -1:
                    count += 1
            if row+1 < ROWS:
                if grid[row+1][col] == 1:
                    grid[row+1][col] = -1
                    count += 1
                    q.append((row+1,col))
                elif grid[row+1][col] == -1:
                    count += 1
            if col-1 >= 0:
                if grid[row][col - 1] == 1:
                    grid[row][col - 1] = -1 
                    count += 1
                    q.append((row,col - 1))
                elif grid[row][col - 1] == -1:
                    count += 1
            if col+1 < COLS:
                if grid[row][col+1] == 1:
                    grid[row][col+1] = -1
                    count += 1
                    q.append((row,col+1))
                elif grid[row][col+1] == -1:
                    count += 1
            
            self.perimeter += (4 - count)


        return self.perimeter


