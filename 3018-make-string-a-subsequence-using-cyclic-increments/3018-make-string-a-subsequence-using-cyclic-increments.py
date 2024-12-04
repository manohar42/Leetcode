class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        if len(str2) > len(str1):
            return False
        
        str_2_list = list(str2)
        n = len(str1)-1
        while str_2_list and n >= 0:
            k = str_2_list.pop()
            value = ord(str1[n])
            value_1 = value+1
            if value_1 > 122:
                value_1 = 97

            if value == ord(k) or value_1 == ord(k):
                n-=1
                continue
            n-=1
            str_2_list.append(k)
        # print(str_2_list)
        if len(str_2_list) == 0:
            return True
        return False