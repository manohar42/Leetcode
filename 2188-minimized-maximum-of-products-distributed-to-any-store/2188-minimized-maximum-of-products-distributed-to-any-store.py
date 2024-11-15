class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        

        

        left = 1
        right = max(quantities)

        while left < right:

            mid = (left+right)//2
            val = 0

            for i in quantities:
                val+= math.ceil(i/mid)
            if val <= n:
                right = mid
            else:
                left = mid+1
        return left