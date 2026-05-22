class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        from collections import deque

        dq = deque()
        result = []

        for right in range(0,len(nums)):

            if dq and dq[0] < right-k+1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if right>=k-1:
                result.append(nums[dq[0]])
        return result