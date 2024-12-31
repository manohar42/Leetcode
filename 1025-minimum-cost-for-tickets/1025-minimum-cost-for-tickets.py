class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [-1]*len(days)
        def dfs(i):
            if i >= len(days):
                return 0
            # print(dp[:])
            # print(cur_cost)
            if dp[i] != -1:
                return dp[i]
            # print(dp)
            pos_2 = days[i]+7-1
            pos_3 = days[i]+30-1
            d_2 = i
            while d_2 < len(days) and days[d_2] <= pos_2:
                d_2+=1
            
            d_3 = i
            while d_3 < len(days) and days[d_3] <= pos_3:
                d_3+=1

            dp[i] = min(costs[0]+dfs(i+1),costs[1]+dfs(d_2),costs[2]+dfs(d_3))

            return dp[i]
            

        
        return dfs(0)
            
