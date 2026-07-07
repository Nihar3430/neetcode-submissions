class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_list = [0] * 26
        l = 0
        r = 0
        res = 0

        while r < len(s):
            freq_list[ord(s[r]) - ord('A')] = freq_list[ord(s[r]) - ord('A')] + 1

            replacements = (r - l + 1) - max(freq_list)

            if replacements <= k:
                res = max(res, r - l + 1)
                r = r+1
            else:
                freq_list[ord(s[l]) - ord('A')] = freq_list[ord(s[l]) - ord('A')] - 1
                l += 1
                r += 1
            
        return res