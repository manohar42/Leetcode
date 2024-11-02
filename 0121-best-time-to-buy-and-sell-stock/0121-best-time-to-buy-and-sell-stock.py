class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        p = prices[0]
        profit = 0
        for i in range(0,n):
            if prices[i] < p:
                p = prices[i]
            profit = max(profit,prices[i] - p)
        return profit
