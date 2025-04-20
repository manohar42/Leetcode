class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        hashmap = defaultdict()
        min_count = 0
        for i in range(0,len(answers)):
            hashmap[answers[i]] = hashmap.get(answers[i],0)+1
            if answers[i]+1 == hashmap[answers[i]]:
                min_count+= hashmap[answers[i]]
                hashmap[answers[i]] = 0
            
        for i in hashmap:
            if hashmap[i]!=0:
                min_count+=i+1
        return min_count