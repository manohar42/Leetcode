class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def check(s1,s2):
            if len(s1)!= len(s2):
                return False
            count = 1
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count-=1
                    if count < 0:
                        return False
            return True


        n = len(words)
        dp = [1] *n
        
        prev = [-1]*n
        max_index = 0
        for i in range(1,n):
            for j in range(i):
                if (groups[i]!=groups[j] and dp[i] < dp[j]+1 and check(words[i],words[j])):
                    dp[i]=dp[j]+1
                    prev[i]=j
                if dp[i] > dp[max_index]:
                    max_index = i
        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev[i]
        ans.reverse()
        return ans
