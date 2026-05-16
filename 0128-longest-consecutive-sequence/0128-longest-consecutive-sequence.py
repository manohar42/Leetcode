class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        s = set(nums)

        longest = 1
        if len(nums)==0:
            return 0

        for num in s:

            if num-1 not in s:
                length=1
                next_num = num+1
                while next_num in s:
                    next_num+=1
                    length+=1
                longest = max(longest,length)
        return longest