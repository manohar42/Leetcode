class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        current = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0)+1
            current[i] =0
        elements = set()
        sol = list()
        prev = 0
        n = len(s)
        for i in range(0,n):
            current[s[i]] +=1
            elements.add(s[i])
            flag = True
            for e in elements:
                if current[e] < hashmap[e]:
                    flag = False
                    break
            if flag == True:
                e = set()
                length = i-prev+1
                sol.append(length)
                prev = i+1
        return sol