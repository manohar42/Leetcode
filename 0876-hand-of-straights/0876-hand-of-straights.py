class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)

        if n%groupSize != 0:
            return False

        hand.sort()
        hashmap = Counter(hand)

        while hashmap:

            min = next(iter(hashmap))

            for j in range(min,min+groupSize):
                if j not in hashmap or hashmap.get(j,0) == 0:
                    return False
                hashmap[j]-=1
                if hashmap[j] == 0:
                    hashmap.pop(j)
        return True