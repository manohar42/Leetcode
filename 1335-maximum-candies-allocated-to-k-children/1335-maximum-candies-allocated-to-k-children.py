class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def check(candies,mid,k):
            count = 0
            for i in candies:
                count+= i//mid
            # print(count,k)
            if count>=k:
                return True
            return False
        left = 0
        right = max(candies)

        if sum(candies) < k:
            return 0
        while left < right:
            mid = (left+right+1)//2
            
            if check(candies,mid,k):
                left=mid
            else:
                right=mid -1
        
        return right 
