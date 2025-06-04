class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        k = len(word)

        prev = "a"
        i = 0
        if numFriends == 1:
            return word
        max_res_len = k - numFriends+1
        for i in range(0,k-max_res_len):
            if prev < word[i:max_res_len+i]:
                prev = word[i:max_res_len+i]
        for i in range(k-max_res_len,k):
            if prev < word[i:]:
                prev = word[i:]
        return prev