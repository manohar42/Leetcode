class Solution:
    def climbStairs(self, n: int) -> int:

        curr,prev = 1,1

        for i in range(1,n):
            temp = curr
            curr = curr+prev
            prev = temp
        return curr
        