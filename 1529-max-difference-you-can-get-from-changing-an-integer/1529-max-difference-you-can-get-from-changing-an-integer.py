class Solution:
    def maxDiff(self, num: int) -> int:
        
        s = str(num)
        rep = ""
        for i in range(0,len(s)):
            if s[i] != '9':
                rep += s[i]
                break
        if rep == "":
            rep +="9"
        max_val = s.replace(rep,'9')
        s_rep = ""
        if s[0] == '1':
            for i in range(1,len(s)):
                if s[i] != '1' and s[i] != '0':
                    s_rep += s[i]
                    min_val = s.replace(s[i],'0')
                    break
            if s_rep == "":
                min_val = s
        else:
            s_rep +="1"
            min_val = s.replace(s[0],s_rep,)
        # print(max_val,min_val)
        return int(max_val) - int(min_val)
    