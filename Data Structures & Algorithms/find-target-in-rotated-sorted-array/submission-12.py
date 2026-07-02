class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        deflection = 0

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid
            else:
                deflection = r
                break

        l = 0
        r = len(nums) - 1
        if target >= nums[deflection] and target <= nums[r]:
            l = deflection
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return -1
        else:
            r = deflection
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return -1
                




