class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        def generateStrings(n,s):
            if len(s) == n:
                if s not in nums:
                    return s
                else:
                    return None
            
            for i in ["0","1"]:
                if len(s) == 0:
                    k = generateStrings(n,i)
                else:
                    k = generateStrings(n,s+i)
                if k is not None:
                        break
            return k                


        return generateStrings(n,'')