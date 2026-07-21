from collections import defaultdict

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])


        atlanticvisited = set()

        def dfsAtlantic(r,c):
            if (r,c) in atlanticvisited:
                return
            atlanticvisited.add((r,c))

            if r + 1 < ROWS and heights[r+1][c] >= heights[r][c]:
                dfsAtlantic(r+1,c)
            if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                dfsAtlantic(r-1,c)
            if c + 1 < COLS and heights[r][c+1] >= heights[r][c]:
                dfsAtlantic(r,c+1)
            if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                dfsAtlantic(r,c-1)



        pacificvisited = set()

        def dfsPacific(r,c):
            if (r,c) in pacificvisited:
                return
            pacificvisited.add((r,c))

            if r + 1 < ROWS and heights[r+1][c] >= heights[r][c]:
                dfsPacific(r+1,c)
            if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                dfsPacific(r-1,c)
            if c + 1 < COLS and heights[r][c+1] >= heights[r][c]:
                dfsPacific(r,c+1)
            if c - 1 >= 0  and heights[r][c-1] >= heights[r][c]:
                dfsPacific(r,c-1)

        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0:
                    dfsPacific(r,c)
                if c == 0:
                    dfsPacific(r,c)
                if r == len(heights) - 1:
                    dfsAtlantic(r,c)
                if c == len(heights[0]) - 1:
                    dfsAtlantic(r,c)


        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):

                if (r,c) in pacificvisited and (r,c) in atlanticvisited:
                    res.append(list((r,c)))

        return res
