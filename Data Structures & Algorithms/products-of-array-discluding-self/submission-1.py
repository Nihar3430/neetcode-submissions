class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        prefix_sum = []
        prefix_sum.append(nums[0])

        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] * prefix_sum[i-1])

        suffix_sum = []
        suffix_sum.append(nums[len(nums) - 1])

        for i in range(len(nums) - 1, 0, -1):
            suffix_sum.append(nums[i - 1] * suffix_sum[-1])

        suffix_sum.reverse()
        
        for i in range(len(nums)):
            if i == 0:
                output.append(suffix_sum[i + 1])
            elif i == len(nums) - 1:
                output.append(prefix_sum[i - 1])
            else:
                output.append(prefix_sum[i - 1] * suffix_sum[i + 1])

        return output
