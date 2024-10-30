class Solution:
    def isValid(self, s: str) -> bool:
        
        closedList = [")","}","]"]
        if s[0] in closedList:
            return False
        stack = []

        for i in s:
            if i not in closedList:
                stack.append(i)
            else:
                if stack == []:
                    return False
                k = stack.pop()
                if (i == "}" and k == "{") or ( i == ")" and k == "(" ) or (i == "]" and k == "["):
                    pass
                else:
                    return False
        if stack == []:
            return True
        return False