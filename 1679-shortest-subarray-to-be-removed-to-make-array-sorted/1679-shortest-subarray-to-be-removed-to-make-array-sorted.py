class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        
        arr.append(float('inf'))
        arr.insert(0,0)
        n = len(arr)
        left = 0
        right = len(arr)-1
        while left+1 < n and arr[left] <= arr[left+1]:
                left+=1
        if left == n-1:
            return 0
        shortest = float('inf')
        # while right >0:
        #     if arr[right]

        while left >= 0:
            while left <= right and arr[left] <= arr[right]:
                if right+1 == n:
                    right-=1
                elif arr[right] <= arr[right+1]:
                    right-=1
                else:
                    break
            # print("Left",left)
            shortest = min(shortest, right-left)
            # print(shortest)
            left-=1
        return shortest