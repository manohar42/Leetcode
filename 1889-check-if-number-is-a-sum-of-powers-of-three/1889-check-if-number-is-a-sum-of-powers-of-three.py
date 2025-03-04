class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        lis = list()
        lis.append(1)
        value = 1
        for i in range(1,17):
            value *=3
            lis.append(value)
        # print(lis)
        for i in range(len(lis)-1,-1,-1):
            if n >= lis[i]:
                n-=lis[i]
                if n==0:
                    return True
        return False