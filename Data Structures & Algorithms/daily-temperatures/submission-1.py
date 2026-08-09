class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for t in range(len(temperatures))]

        for i in range(len(temperatures)):
            while(len(stack) > 0 and stack[-1][0] < temperatures[i]):
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        
        return res