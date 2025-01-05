class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        lis = list(s)
        c_list = [0 for _ in range(len(s)+1)]
        for i,j, d in shifts:
            if d == 0:
                c_list[i]-=1
                c_list[j+1] +=1
            else:
                c_list[i]+=1
                c_list[j+1]-=1
        c_sum = 0

        for i in range(0,len(s)):
            c_sum+=c_list[i]

            lis[i] = chr((((ord(lis[i])+ c_sum)-97)%26)+97)
        return ''.join(lis)
