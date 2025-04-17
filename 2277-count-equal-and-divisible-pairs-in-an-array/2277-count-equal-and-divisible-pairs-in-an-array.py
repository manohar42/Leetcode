class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        hashmap = defaultdict(list)
        count = 0
        for i in range(0,len(nums)):
            if nums[i] in hashmap:
                for j in hashmap[nums[i]]:
                    if j*i %k == 0:
                        count+=1
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]].append(i)
        return count