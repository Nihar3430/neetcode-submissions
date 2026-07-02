class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        count = {}
        for i in range(len(nums) + 1):
            buckets.append([])

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for i,j in count.items():
            buckets[j].append(i)

        result = []

        for i in reversed(buckets):
            for j in i:
                if k > 0:
                    result.append(j)
                k -= 1

        return result