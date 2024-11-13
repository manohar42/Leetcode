class Solution:
    def maximumSwap(self, num: int) -> int:
        

        lis = list(map(int, str(num)))
        # print(lis)
        hashmap = {value:index for index,value in enumerate(lis)}

        # print(hashmap)
        for i,digit in enumerate(lis):
            # print(i)
            for j in range(9,digit,-1):
                if hashmap.get(j,-1) > i:
                    # print(j,lis[i])
                    lis[i],lis[hashmap[j]] = lis[hashmap[j]], lis[i]
                    return int("".join(map(str,lis)))
        return num
