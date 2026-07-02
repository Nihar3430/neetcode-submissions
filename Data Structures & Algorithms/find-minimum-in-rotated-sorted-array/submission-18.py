class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0

        while l <= r:
            mid = (r+l)//2

            if nums[mid] < nums[r]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid
            else:
                return nums[r]