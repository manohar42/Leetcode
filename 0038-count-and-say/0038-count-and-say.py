class Solution:
    def countAndSay(self, n: int) -> str:
        arr = []
        s = "1"
        for i in range(1,n):
            j = 0
            arr = []
            while j < len(s):
                count = 1
                while j+1<len(s) and s[j] == s[j+1]:
                    count+=1
                    j+=1
                else:
                    j+=1
                arr.append([count,s[j-1]])
            s = ""
            for k in arr:
                s+=str(k[0])+str(k[1])
         
        return s


