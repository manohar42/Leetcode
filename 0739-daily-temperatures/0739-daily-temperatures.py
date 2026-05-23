class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0]*len(temperatures)

        for i in range(0,len(temperatures)):
            if i == 0:
                stack.append((temperatures[i],i))
                continue
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i-stack[-1][1]
                
                stack.pop()
            stack.append((temperatures[i],i))
        
        return res