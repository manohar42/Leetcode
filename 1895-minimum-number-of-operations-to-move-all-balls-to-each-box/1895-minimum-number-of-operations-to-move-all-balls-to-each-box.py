class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        left_sum = [0 for _ in range(0,n)]
        right_sum = [0 for _ in range(0,n)]
        box_sum = 0
        for i in range(n-2,-1,-1):
            box_sum += int(boxes[i+1])
            left_sum[i] += left_sum[i+1]+box_sum
        # print(left_sum)
        box_sum = 0
        for i in range(1,n):
            box_sum+=int(boxes[i-1])
            right_sum[i] +=right_sum[i-1]+box_sum
        res = [0 for _ in range(0,n)]
        for i in range(0,n):
            res[i] = left_sum[i]+right_sum[i]
        return res