class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)

        length = 0

        for i in mySet:
            if (i - 1) in mySet:
                continue
            
            temp_length = 1

            while (i + temp_length) in mySet:
                temp_length += 1

            length = max(length, temp_length)
        

        return length