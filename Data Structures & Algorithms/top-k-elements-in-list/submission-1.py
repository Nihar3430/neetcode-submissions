class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}

        buckets = [[] for i in range(n + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for i,j in count.items():
            buckets[j].append(i)


        ans = []

        for i in reversed(buckets):
            if k > 0:
                if not i:
                    continue

                for j in i:
                    ans.append(j)
                    k = k-1
            else:
                break


        return ans