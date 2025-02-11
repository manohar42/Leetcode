class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for i in range(0,len(s)):
            if s[i].isdigit():
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)