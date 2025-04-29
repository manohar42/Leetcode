class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        right = 0
        count = 0
        max_value = max(nums)
        max_count = 0
        n = len(nums)
        for i in range(0,n):
            
            if i > 0:
                # print("Nums",nums[i-1],max_value)
                if nums[i-1] == max_value:
                    max_count-=1
            # print(max_count)
            while right < n and max_count < k:
                if nums[right] == max_value:
                    max_count+=1
                right+=1
            # print(i,right,max_count)
            if max_count == k:
                count+= n-right+1
        return count
        