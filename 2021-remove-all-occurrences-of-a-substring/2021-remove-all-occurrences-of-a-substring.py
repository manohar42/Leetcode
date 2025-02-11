class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []
        k = part[-1]
        part_list = list(part)
        n = len(part)
        # print(part_list)
        for i in range(0,len(s)):

            if s[i] == k:
                # print(stack[-(n-1):],"Before")
                # print(stack[-(n-1):] == part_list)
                if n == 1:
                    continue
                if len(stack) >= n-1 and stack[-(n-1):]== part_list[:n-1]:
                    for i in range(0,n-1):
                        stack.pop()
                else:
                    stack.append(s[i])
                # print(stack[-(n-1):],"After")
            else:
                stack.append(s[i])
        return "".join(stack)

