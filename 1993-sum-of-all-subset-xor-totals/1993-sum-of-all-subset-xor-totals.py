class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def recursion(nums,i,subset):
            if i == len(nums):
                return subsets.append(subset[:]) 
            subset.append(nums[i])
            recursion(nums,i+1,subset)
            subset.pop()
            recursion(nums,i+1,subset)

        recursion(nums,0,[])
        # print(subsets)
        max_sum = 0
        for i in subsets:
            if len(i)>0:
                k = i[0]
                for j in range(1,len(i)):                  
                    k = k^i[j]
                max_sum+=k
        return max_sum


