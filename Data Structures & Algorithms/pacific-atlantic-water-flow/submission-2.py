class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        res = []

        rows = len(heights)
        cols = len(heights[0])
        
        pacific_visited = set()

        def dfs_pacific(r, c):
            if (r,c) in pacific_visited:
                return

            pacific_visited.add((r,c))

            if (r-1) >= 0 and heights[r-1][c] >= heights[r][c]:
                dfs_pacific(r-1,c)
            if (r+1) < rows and heights[r+1][c] >= heights[r][c]:
                dfs_pacific(r+1,c)
            if (c-1) >= 0 and heights[r][c-1] >= heights[r][c]:
                dfs_pacific(r,c-1)
            if (c+1) < cols and heights[r][c+1] >= heights[r][c]:
                dfs_pacific(r,c+1)

        
        atlantic_visited = set()

        def dfs_atlantic(r, c):
            if (r,c) in atlantic_visited:
                return

            atlantic_visited.add((r,c))

            if (r-1) >= 0 and heights[r-1][c] >= heights[r][c]:
                dfs_atlantic(r-1,c)
            if (r+1) < rows and heights[r+1][c] >= heights[r][c]:
                dfs_atlantic(r+1,c)
            if (c-1) >= 0 and heights[r][c-1] >= heights[r][c]:
                dfs_atlantic(r,c-1)
            if (c+1) < cols and heights[r][c+1] >= heights[r][c]:
                dfs_atlantic(r,c+1)


        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    dfs_pacific(r, c)
                if c == 0:
                    dfs_pacific(r, c)
                if r == rows - 1:
                    dfs_atlantic(r, c)
                if c == cols - 1:
                    dfs_atlantic(r, c)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_visited and (r,c) in atlantic_visited:
                    res.append(list((r,c)))

        return res
