class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        myDict = {}

        for index, i in enumerate(nums):
            difference = target - i

            if difference in myDict:
                result.append(myDict[difference])
                result.append(index)
                break

            myDict[i] = index

        return result