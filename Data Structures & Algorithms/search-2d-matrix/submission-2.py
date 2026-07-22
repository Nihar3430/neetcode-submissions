class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.result = False

        hi = 0
        lo = ROWS - 1

        while (hi <= lo):
            mid = (hi + lo) // 2

            if target > matrix[mid][0] and target > matrix[mid][COLS - 1]:
                hi = mid + 1
            elif target < matrix[mid][0] and target < matrix[mid][COLS - 1]:
                lo = mid - 1
            elif target >= matrix[mid][0] and target <= matrix[mid][COLS - 1]:
                l = 0
                r = COLS - 1

                while (l <= r):
                    norm_mid = (l + r) // 2

                    if matrix[mid][norm_mid] == target:
                        self.result = True
                        break
                    elif matrix[mid][norm_mid] < target:
                        l = norm_mid + 1
                    else:
                        r = norm_mid - 1

                break

        return self.result