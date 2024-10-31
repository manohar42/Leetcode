class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []
        hashmap = {"C":"D", "A":"B"}

        for i in s:
            if (i == "D" or i == "B") and len(stack) > 0:
                k = stack[-1]
                if k == "C" and i == "D":
                    stack.pop()
                elif k == "A" and i == "B":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
                