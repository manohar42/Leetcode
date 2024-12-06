class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        set_ban = set(banned)
        count = 0
        sum_count = 0
        for i in range(1,n+1):
            if i in set_ban:
                continue
            sum_count+=i
            if sum_count > maxSum:
                return count
            count+=1
        return count