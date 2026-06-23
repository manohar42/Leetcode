class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        min_que = []
        n = len(nums)
        for i in range(0,n):
            while min_que and len(min_que)+n-i-1>=k and nums[i] < min_que[-1]:
                min_que.pop()
            if len(min_que) < k:
                min_que.append(nums[i])

        return min_que