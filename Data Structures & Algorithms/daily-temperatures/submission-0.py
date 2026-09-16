class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                indx = stack.pop()
                answer[indx] = i - indx

            stack.append(i)

        return answer