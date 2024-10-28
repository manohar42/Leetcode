class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        

        nums.sort()
        num_set = set(nums)
        max_size = -1
        hashmap = {}
        for i in nums:
            k = i
            count = 1
            if i not in hashmap:
                hashmap[k] = 1
                while True:
                    k = k*k
                    if k in num_set:
                        count+=1
                        hashmap[k] = 1
                    else:
                        break
            if count >= 2:
                max_size = max(max_size,count)
        return max_size
