class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        res = []
        hashmap = {}

        for i in digits:
            hashmap[i]= hashmap.get(i,0)+1
        # print(hashmap)
        for i in range(100, 1000,2):
            s = i
            smap = hashmap.copy()
            while i > 0:
                # print(i,smap)
                if i%10 in smap and smap[i%10] > 0:
                    smap[i%10]-=1
                    i=i//10  
                else:
                    break
                if i == 0:
                    res.append(s)

        return res