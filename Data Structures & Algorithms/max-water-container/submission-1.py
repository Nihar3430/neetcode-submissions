class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        area = 0
        r = len(height) - 1

        while l < r:
            tarea = min(height[l], height[r]) * (r-l)

            if height[l] <= height[r]:
                l+=1
            elif height[r] < height[l]:
                r -= 1

            area = max(area, tarea)

        return area