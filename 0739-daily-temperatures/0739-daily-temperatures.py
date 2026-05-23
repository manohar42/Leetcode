class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Now we ONLY store indices, not tuples
        n = len(temperatures)
        res = [0] * n
        
        # We can start from 0 and let the loop handle everything
        for i in range(n):
            # Compare current temp with the temp at the index stored at top of stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            
            # Append just the index
            stack.append(i)
            
        return res