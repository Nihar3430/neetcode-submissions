class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        result = []

        result.append(intervals[0])

        for i in intervals[1:]:
            if i[0] <= result[len(result) - 1][1]:
                result[len(result) - 1][1] = max(result[len(result) - 1][1], i[1])
            else:
                result.append(i)
        return result