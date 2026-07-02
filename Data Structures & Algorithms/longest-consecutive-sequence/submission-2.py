class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mydict = {}
        result = 0

        for index, i in enumerate(nums):
            mydict[i] = index

        for i in mydict.keys():
            temp = 0

            if i - 1 not in mydict:
                temp += 1
                while (i + temp) in mydict:
                    temp += 1

            result = max(result, temp)

        return result