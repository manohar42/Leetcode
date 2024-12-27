class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        
        n =len(values)
        dp = [0]*n

        dp[0] = values[0]
        max_val =0
        for i in range(1,n):
            dp[i] = max(dp[i-1],values[i-1]+i-1)
            max_val = max(max_val, dp[i]+values[i]-i)
        return max_val