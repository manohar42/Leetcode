class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = Counter(s)
        current ={}
        for i in hashmap:
            current[i] = 0
        
        elements = set()
        sol = list()
        prev = 0
        # print(hashmap)
        n = len(s)
        for i in range(0,n):
            current[s[i]]+=1
            elements.add(s[i])
            flag = False
            for e in elements:
                if current[e] == hashmap[e]:
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                length = i-prev+1
                sol.append(length)
                prev = i+1
        return sol