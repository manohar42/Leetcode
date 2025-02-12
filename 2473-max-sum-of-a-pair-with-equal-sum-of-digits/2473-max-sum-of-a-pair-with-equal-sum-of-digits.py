class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def number_sum(n):
            numsum = 0
            while n>0:
                k = n%10
                numsum+=k
                n = n//10
            return numsum
        hashmap = defaultdict(list)
        for i in range(0,len(nums)):
            k = number_sum(nums[i])
            if k in hashmap:
                heappush(hashmap[k],-1*nums[i])
            else:
                heapify(hashmap[k])
                heappush(hashmap[k],-1*nums[i])
           
        max_sum = -1
        # print(hashmap)
        for i in hashmap:
            if len(hashmap[i]) >=2:   
                n1 = heappop(hashmap[i])
                n2 = heappop(hashmap[i])
                # print(n1,n2)
                value_sum = (n1+n2)*(-1)
                max_sum = max(max_sum,value_sum)
        return max_sum
        
            