class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        

        def recursion(coins, amount, index):

            if memo[index][amount] != -1:
                return memo[index][amount]
            if amount == 0:
                memo[index][amount] = 1
                return 1
            if amount < 0:
                return 0
            if index < 0:
                return 0
            
            memo[index][amount] = recursion(coins, amount-coins[index], index)+recursion(coins,amount,index-1)

            return memo[index][amount]
        
        return recursion(coins,amount,len(coins)-1)
