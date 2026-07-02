class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0

        freq_list = [0] * 26

        max_length = 0


        while r < len(s):
            freq_list[ord(s[r]) - ord('A')] = freq_list[ord(s[r]) - ord('A')] + 1

            num_replacements = (r - l + 1) - max(freq_list)

            if num_replacements <= k:
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                freq_list[ord(s[l]) - ord('A')] = freq_list[ord(s[l]) - ord('A')] - 1
                l += 1
                r += 1


        return max_length



