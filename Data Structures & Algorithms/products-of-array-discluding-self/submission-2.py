class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 8 48
        # 48 48 24 6


        prefix_sum = []
        prefix_sum.append(nums[0])

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] * nums[i])

        suffix_sum = []
        suffix_sum.append(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            suffix_sum.append(suffix_sum[-1] * nums[i])

        suffix_sum.reverse()

        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_sum[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix_sum[i - 1])
            else:
                res.append(suffix_sum[i + 1] * prefix_sum[i - 1])

        return res