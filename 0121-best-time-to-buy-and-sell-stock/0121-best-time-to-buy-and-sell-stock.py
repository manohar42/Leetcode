class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        start = 1
        minimum = prices[0]
        end = len(prices)
        profit = 0
        while start < end:
            profit_expected = prices[start]-minimum
            profit = max(profit_expected,profit)
            if minimum > prices[start]:
                minimum = prices[start]
            start+=1
        return profit
            