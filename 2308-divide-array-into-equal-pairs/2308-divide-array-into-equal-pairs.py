class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = {}
        if len(nums)%2 != 0:
            return False
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
        
        for i in hashmap:
            if hashmap[i]%2!=0:
                return False
        return True