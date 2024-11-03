class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        Output_list = []
        for i in strs:
            s= list(i)

            s= sorted(s)
            s = "".join(s)
            if s in hashmap:
                hashmap[s].append(i)
            else:
                hashmap[s] = [i]
        
        for i in hashmap:
            Output_list.append(hashmap[i])
        return Output_list
            
              
        