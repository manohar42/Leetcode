class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        

        nums.sort()
        num_set = set(nums)
        max_size = -1
        hashmap = set()
        for i in nums:
            k = i
            count = 1
            if i not in hashmap:
                hashmap.add(k)
                while True:
                    k = k*k
                    if k in num_set:
                        count+=1
                        hashmap.add(k)
                    else:
                        break
            else:
                continue   
            if count >= 2:
                max_size = max(max_size,count)
        return max_size
