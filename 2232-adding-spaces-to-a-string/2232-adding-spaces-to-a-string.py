class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        start = 0
        result = []
        for i in spaces:
            result.append(s[start:i])
            start = i
        result.append(s[start:])
        
        return " ".join(result)