class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()

        if len(s) == 0:
            return 0

        left = 0
        right = 1
        res = 1
        chars.add(s[left])

        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                chars.remove(s[left])
                left += 1

        return res
            