class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = float('inf')
        for i in strs:
            if len(i) < n:
                n = len(i)

        # print(n)
        start = 0
        s =""
        while start < n:
            k = strs[0][start]
            for i in strs:
                if k == i[start]:
                    continue
                else:
                    return s
            s+=k
            start+=1
        return s

