class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        hashmap = {}
        count = 0
        right = 0
        distinct_count = len(set(nums))
        for i in range(0,len(nums)):
            if i>0:
                hashmap[nums[i-1]]-=1
                if hashmap[nums[i-1]] == 0:
                    hashmap.pop(nums[i-1])
            while right < len(nums) and len(hashmap) < distinct_count:
                hashmap[nums[right]] = hashmap.get(nums[right],0)+1
                right+=1
            if len(hashmap) == distinct_count:
                count+=len(nums)-right+1
        return count
