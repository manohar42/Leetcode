class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        max_luck = -1
        for i in hashmap:
            if hashmap[i] == i and max_luck < i:
                max_luck = i
        return max_luck
