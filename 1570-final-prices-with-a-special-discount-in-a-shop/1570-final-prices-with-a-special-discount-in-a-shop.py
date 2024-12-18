class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        left = 0
        right = 1
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return prices