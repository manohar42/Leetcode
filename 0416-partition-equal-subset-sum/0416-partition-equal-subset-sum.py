class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        if sum(nums)%2 != 0:
            return False
        dp = set()
        dp.add(0)

        n =len(nums)-1
        target = sum(nums)//2

        for i in range(n,-1,-1):
            next_dp = set()
            for j in dp:
                next_dp.add(j+nums[i])
                next_dp.add(j)
                if j == target:
                    return True
            dp = next_dp
        
        return False

