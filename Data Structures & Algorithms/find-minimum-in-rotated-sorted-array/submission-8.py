class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[high] > nums[mid]:
                high = mid
            elif nums[low] < nums[mid]:
                low = mid
            else:
                low = mid + 1
            
        return nums[mid]