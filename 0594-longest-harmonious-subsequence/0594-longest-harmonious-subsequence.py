class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        hashmap = Counter(nums)
        max_sequence = 0
        sequence_count = 0
        for i in hashmap:
            if max(hashmap.get(i-1,0),hashmap.get(i+1,0)):
                sequence_count = max(hashmap.get(i-1,0),hashmap.get(i+1,0))+hashmap[i]
                max_sequence = max(sequence_count,max_sequence)
        
        return max_sequence