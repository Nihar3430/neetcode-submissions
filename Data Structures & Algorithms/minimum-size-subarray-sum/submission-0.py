class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0

        res = float('inf')
        total = nums[r]

        while r < len(nums):
            if total < target:
                if r + 1 >= len(nums):
                    break
                r += 1
                total += nums[r]
            elif total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if res == float('inf') else res