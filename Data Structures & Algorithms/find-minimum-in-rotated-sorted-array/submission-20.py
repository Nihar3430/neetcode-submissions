class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = (r+l) // 2

            if nums[l] < nums[mid]:
                l = mid
            elif nums[r] > nums[mid]:
                r = mid
            else:
                break
            
        return nums[r]