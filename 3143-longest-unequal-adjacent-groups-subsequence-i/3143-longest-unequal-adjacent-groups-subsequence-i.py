class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        sequence_0 = []
        sequence_1 = []
        value = 0
        n = len(groups)
        for i in range(0,n):
            if value == groups[i]:
                sequence_0.append(i)
                if value ==1:
                    value = 0
                else:
                    value = 1
        value = 1
        for i in range(0,n):
            if value == groups[i]:
                sequence_1.append(i)
                if value ==1:
                    value = 0
                else:
                    value = 1
        sequence = sequence_1 if len(sequence_1) > len(sequence_0) else sequence_0

        res = []

        for i in sequence:
            res.append(words[i])
        return res

