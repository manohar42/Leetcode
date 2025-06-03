class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        queue = deque()
        n = len(status)
        AvailableBoxes = {i:0 for i in range(len(status))}
        Total_candies = 0
        # print(type(keys))

        for i in initialBoxes:
            if status[i] == 1:
                queue.append(i)
            else:
                AvailableBoxes[i]=1
        while queue:
            box = queue.pop()
            for i in keys[box]:
                status[i] = 1
            for i in AvailableBoxes:
                if status[i] == 1 and AvailableBoxes[i] ==1:
                    queue.append(i)
                    AvailableBoxes[i] = 0
            for i in containedBoxes[box]:
                if status[i] == 1:
                    queue.append(i)
                else:
                    AvailableBoxes[i] = 1
            Total_candies+=candies[box]
        return Total_candies
            