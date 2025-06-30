class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        hashmap = Counter(nums)
        print(hashmap)
        max_sequence = 0
        sequence_count = 0
        for i in range(0,len(nums)):
            if max(hashmap.get(nums[i]-1,0),hashmap.get(nums[i]+1,0)):
                sequence_count = max(hashmap.get(nums[i]-1,0),hashmap.get(nums[i]+1,0))+hashmap[nums[i]]
                max_sequence = max(sequence_count,max_sequence)
        
        return max_sequence