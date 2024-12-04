class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        if len(str2) > len(str1):
            return False
        
        m = len(str2)-1
        n = len(str1)-1
        while m>=0 and n >= 0:
            k = str2[m]
            value = ord(str1[n])
            value_1 = value+1
            if value_1 > 122:
                value_1 = 97

            if value == ord(k) or value_1 == ord(k):
                n-=1
                m-=1
                continue
            n-=1
            
        print(m)
        if m < 0:
            return True
        return False