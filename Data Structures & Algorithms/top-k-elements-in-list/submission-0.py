class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for key, value in count.items():
            freq[value].append(key)

        for i in freq[::-1]:
            for j in i:
                if k > 0:
                    result.append(j)
                    k -= 1

        return result