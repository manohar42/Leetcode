class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        hashmap = Counter(nums)
        max_value = 0
        dominant_element = 0
        for i in hashmap:
            if hashmap[i]>max_value:
                max_value =hashmap[i]
                dominant_element = i
        count = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] == dominant_element:
                count+=1
            if count/(i+1) > 0.5 and ((n-i-1)>0 and (max_value-count)/(n-i-1) > 0.5):
                return i
        return -1
