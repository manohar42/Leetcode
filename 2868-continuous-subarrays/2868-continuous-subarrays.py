class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        max_queue = deque()
        min_queue = deque()

        l = 0
        n = len(nums)
        ans = 0
        for right in range(n):
            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            
            min_queue.append(nums[right])
            max_queue.append(nums[right])

            while min_queue and max_queue and (max_queue[0] - min_queue[0] > 2):
                if nums[l] == max_queue[0]:
                    max_queue.popleft()
                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                l+=1
            ans+=(right-l+1)
        return ans

