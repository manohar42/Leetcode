class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        
        n = len(arr)
        i=0
        count = 0
        while i < n:
            if arr[i] &1 == 1:
                count+=1
            else:
                count =0
            if count ==3:
                return True
            i+=1

        return False
