class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}

        for i in s:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        for j in t:
            if j in myDict:
                if myDict[j] <= 0:
                    return False
                else:
                    myDict[j] -= 1
            else:
                return False
        
        for k in myDict:
            if myDict[k] != 0:
                return False

        return True