class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for i,j in count.items():
            buckets[j].append(i)

        result = []

        for i in reversed(buckets):
            if k > 0 and i:
                for j in i:
                    result.append(j)
                    k -= 1
            

        return result