class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        

        n = len(nums)

        if n%k != 0:
            return False

        nums.sort()
        hashmap = Counter(nums)

        while hashmap:

            min = next(iter(hashmap))

            for j in range(min,min+k):
                if j not in hashmap or hashmap.get(j,0) == 0:
                    return False
                hashmap[j]-=1
                if hashmap[j] == 0:
                    hashmap.pop(j)
        return True