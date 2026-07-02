class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # "michael" {[1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,010,0,1,0,0,0,0,0,0,0]: []}
        alphabet = [0] * 26
        mydict = {}

        for s in strs:
            for c in s:
                ascii = ord(c) - 97
                alphabet[ascii] += 1

            if tuple(alphabet) in mydict:
                mydict[tuple(alphabet)].append(s)
            else:
                mydict[tuple(alphabet)] = [s]
            alphabet = [0] * 26

        ans = []
        
        for i,j in mydict.items():
            ans.append(j)

        return ans