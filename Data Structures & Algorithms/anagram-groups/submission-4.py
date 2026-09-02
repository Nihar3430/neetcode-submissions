from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #97
        alphabet = [0] * 26
        alph_dict = defaultdict(list)

        for word in strs:
            for char in word:
                alphabet[ord(char) - 97] += 1
            alph_dict[tuple(alphabet)].append(word)
            alphabet = [0] * 26

        res = []
        for v in alph_dict.values():
            res.append(v)

        return res


