class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = [0]*len(questions)

        for i in range(len(questions)-1,-1,-1):
            if questions[i][1]+i+1 >len(questions)-1:
                dp[i] = questions[i][0]
                if i < len(questions)-1:
                    dp[i] = max(dp[i+1],dp[i])
            else:
                k = i+ questions[i][1]+1
                dp[i] = max(dp[i+1],questions[i][0]+dp[k])
        return dp[0]