
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        myset =  set()

        for num in nums:
            myset.add(num)

        for num in myset:
            if (num - 1) not in myset:
                count = 1
                new_num = num
                while (new_num+1) in myset:
                    count += 1
                    new_num += 1
                res = max(res,count)
                

        return res
            