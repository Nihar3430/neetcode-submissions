class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_sum = [1] * n

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1]

        suffix_sum = [1] * n

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] * nums[i+1]


        ans = []

        for i in range(n):
            ans.append(prefix_sum[i] * suffix_sum[i])

    
        return ans