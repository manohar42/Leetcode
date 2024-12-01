class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        n = len(arr)
        hashmap = {}
        for i in range(n):
            hashmap[arr[i]*2] = i

        for i in range(n):
            if arr[i] in hashmap and hashmap[arr[i]]!= i:
                return True
        return False