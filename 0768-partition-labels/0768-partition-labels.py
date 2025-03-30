class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = Counter(s)
        current ={}
        elements = set()
        sol = list()
        prev = 0
        n = len(s)
        for i in range(0,n):
            current[s[i]] = current.get(s[i],0)+1
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