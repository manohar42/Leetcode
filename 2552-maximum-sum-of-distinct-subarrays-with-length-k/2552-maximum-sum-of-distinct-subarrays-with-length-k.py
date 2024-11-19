class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        left = 0
        right = 0
        n = len(nums)
        hashmap ={}
        sum_value = 0
        max_value = 0
        while right < n:
            if right-left <= k-1:
                # print(hashmap, nums[right],hashmap.get(nums[right],-1))
                if hashmap.get(nums[right],-1) < 0:
                    hashmap[nums[right]]=right
                    sum_value += nums[right]
                else:
                    while left <= hashmap[nums[right]]:
                        sum_value -=nums[left]
                        left +=1
                    hashmap[nums[right]] = right
                    
                    sum_value +=nums[right]
                    # print("Sum_value",sum_value)
                    hashmap[nums[left]]= 1
                # print(sum_value)
            # print(sum_value,hashmap)
            if right-left == k-1:
                max_value = max(max_value, sum_value)
                sum_value = sum_value - nums[left]
                hashmap[nums[left]] = 0
                left+=1
                
            right+=1
            # print(left,right)
        return max_value



