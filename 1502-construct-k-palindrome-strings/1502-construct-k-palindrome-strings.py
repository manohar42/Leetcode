class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        arr = [0 for _ in range(0,26)]
        count = 0
        n = len(s)
        if n <k:
            return False
        for i in s:
            # print(ord(i)-ord('a'))
            arr[ord(i)-ord('a')] +=1
        for j in arr:
            if j%2 != 0:
                count+=1
            if count > k:
                return False
        return True