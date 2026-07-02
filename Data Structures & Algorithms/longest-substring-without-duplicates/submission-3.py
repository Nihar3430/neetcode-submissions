class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1

        duplicates = set()

        if len(s) == 0:
            return 0

        duplicates.add(s[l])
        max_length = 1

        while r < len(s):
            if s[r] not in duplicates:
                duplicates.add(s[r])
                max_length = max(max_length, r-l+1)
                r += 1
            else:
                duplicates.discard(s[l])
                l += 1

        return max_length
