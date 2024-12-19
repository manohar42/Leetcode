class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        chunk= "ended"
        chunk_start = 0
        count = 0
        n = len(arr)
        res = 0
        for i in range(n):
            res+=1
            if chunk == "ended"and arr[i] == i:
                count+=1                
            else:
                if chunk_start < arr[i]:
                    chunk_start = arr[i]
                if res-1 == chunk_start:
                    chunk = "ended"
                else:
                    if chunk == "ended":
                        chunk = "started"
                        count+=1
                # print(chunk,count)
        return count


