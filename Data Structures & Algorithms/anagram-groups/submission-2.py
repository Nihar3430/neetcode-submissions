class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mydict = {}
        alphabet = [0] * 26

        for i in strs:
            for j in i:
                alphabet[97 - ord(j)] = alphabet[97 - ord(j)] + 1

            if tuple(alphabet) not in mydict:
                mydict[tuple(alphabet)] = [i]
            else:
                mydict[tuple(alphabet)].append(i)
            alphabet = [0] * 26

        result = []

        for i,j in mydict.items():
            result.append(j)


        return result