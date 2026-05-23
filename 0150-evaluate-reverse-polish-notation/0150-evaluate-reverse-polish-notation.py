class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric():
                stack.append(int(i))
            else:
                if i.startswith('-') and i.lstrip('-').isdigit():
                    stack.append(int(i))
                    continue
                   
                # print(stack,i)
                l = stack.pop()
                r =stack.pop()
                if i == "+":   
                    res = l+r
                    stack.append(res)
                elif i == "-":
                    res = r-l
                    stack.append(res)
                elif i == "/":
                    res = r/l
                    if res > 0:
                        res = floor(res)
                    else:
                        res = ceil(res)
                    stack.append(res)
                elif i == "*":
                    res = l*r
                    stack.append(res)
            
        # print(stack)

        return stack[0]