from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        result = []

        for i in strs:
            alphabet = [0] * 26
            for j in i:
                alphabet[ord(j) - ord('a')] += 1
            
            mydict[tuple(alphabet)].append(i)

        for i in mydict.values():
            result.append(i)

        return result
