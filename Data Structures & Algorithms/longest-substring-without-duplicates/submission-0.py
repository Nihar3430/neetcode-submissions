class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        myset = set()
        count = 0


        while r < len(s):
            if s[r] not in myset:
                myset.add(s[r])
                r+=1
            else:
                myset.remove(s[l])
                l+=1

            count = max(count, r - l)
                
        return count