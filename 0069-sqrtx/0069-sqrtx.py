class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 1
        right = x
        if x == 0:
            return 0
        # if x== 1:
        #     return 1

        while left <= right:
            mid = (left+right)//2
            # print(mid)
            if mid == x//mid:
                return mid
            elif mid > x//mid:
                right = mid-1
            else:
                left = mid+1
            # print(mid,left,right)
        return right
        