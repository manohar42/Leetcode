class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        
        n = len(arr)
        i=0
        while i < n:
            if arr[i]%2!=0 and i+2 < n:
                if arr[i+1]%2!=0 and arr[i+2]%2!=0:
                    return True
            i+=1
        return False
