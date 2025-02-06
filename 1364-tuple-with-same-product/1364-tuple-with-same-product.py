class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        hashmap = {}
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                k = nums[i]*nums[j]
                hashmap[k] = hashmap.get(k,0) + 1      
        count = 0
        for i in hashmap:
            if hashmap[i] > 1:
                number_of_ways = hashmap[i]*(hashmap[i]-1)*4
                count += number_of_ways
        return count