class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        chunk= "ended"
        chunk_start = 0
        count = 0
        n = len(arr)
        res = []
        for i in range(n):
            res.append(arr[i])
            if chunk == "ended"and arr[i] == i:
                count+=1                
            else:
                if chunk_start < arr[i]:
                    chunk_start = arr[i]
                if len(res)-1 == chunk_start:
                    chunk = "ended"
                else:
                    if chunk == "ended":
                        chunk = "started"
                        count+=1
                # print(chunk,count)
        return count


