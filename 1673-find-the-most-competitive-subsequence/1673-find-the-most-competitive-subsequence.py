class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        min_que = []

        for i in range(0,len(nums)):
            while min_que and len(nums)-i-1>=k-len(min_que) and nums[i] < min_que[-1]:
                min_que.pop()
            if len(min_que) < k:
                min_que.append(nums[i])
        
        # res = []

        # while len(min_que)>0:
        #     res.append(min_que.popleft())

        return min_que