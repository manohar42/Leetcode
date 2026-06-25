class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        hashmap = {}
        hashmap['('] =  n
        hashmap[')'] = n
        result = []

        def backtrack(curr,hashmap):

            if hashmap['('] == 0 and hashmap[')'] == 0:
                result.append(''.join(curr[:]))
                return
            
            for  i in hashmap:
                if i == ")" and hashmap['('] >= hashmap[')']:
                    
                    continue

                if hashmap[i] > 0:
                    curr.append(i)
                    hashmap[i]-=1
                    backtrack(curr,hashmap)
                    hashmap[i]+=1
                    curr.pop()
        backtrack([],hashmap)

        return result

                        
