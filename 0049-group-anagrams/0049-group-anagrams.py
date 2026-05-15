class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for i in strs:

            s= list(i)

            s.sort()
            j = ''.join(s)
            if j in hashmap:
                hashmap[j].append(i)
            else:
                hashmap[j] = [i]
        result = []
        for i in hashmap:
            result.append(hashmap[i])
        return result
            