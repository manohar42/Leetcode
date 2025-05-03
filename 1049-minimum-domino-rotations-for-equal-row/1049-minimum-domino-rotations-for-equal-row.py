class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def check(value,arr1,arr2):
            n = len(arr1)
            count = 0
            for i in range(0,n):
                if arr1[i] != value:
                    if arr2[i] != value:
                        return -1
                    else:
                        count+=1
            return count
        result = [0,0,0,0]
        result[0] = check(tops[0],tops,bottoms)
        result[1] = check(bottoms[0],bottoms,tops)
        result[2] = check(tops[0],bottoms,tops)
        result[3]= check(bottoms[0],tops,bottoms)
        n = 3
        # print(result)
        min_val = float('inf')
        while n >= 0:
            if result[n] != -1 and result[n]<min_val:
                min_val = result[n]
            n-=1
        if min_val == float('inf'):
            return -1
        else:
            return min_val