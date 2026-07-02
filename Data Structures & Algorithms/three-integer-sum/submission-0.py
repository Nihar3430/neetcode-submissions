class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for index, i in enumerate(nums):
            if index > 0 and i == nums[index - 1]:
                continue

            l = index + 1
            r = len(nums) - 1

            while l < r:

                if i + nums[l] + nums[r] > 0:
                    r = r - 1
                elif i + nums[l] + nums[r] < 0:
                    l = l + 1
                elif i + nums[l] + nums[r] == 0:
                    res.append([i, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res