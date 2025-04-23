class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = {}
        def sumofdigits(val):
            k = val
            sum_val = 0
            while k > 0:
                sum_val+=k%10
                k = k//10
            return sum_val
        max_value = 0
        count = 0
        for i in range(1,n+1):
            k = sumofdigits(i)
            hashmap[k] = hashmap.get(k,0)+1
            max_value = max(hashmap[k],max_value)
        # print(hashmap)
        for i in hashmap:
            if hashmap[i] == max_value:
                count+=1
        return count