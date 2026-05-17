class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = [height[0]]
        left = height[0]
        right_max = [height[-1] for i in range(0,len(height))]
        right = height[-1]
        result = []

        for i in range(1,len(height)):
            
            if height[i] > left:
                left_max.append(height[i])
                left = height[i]
            else:
                left_max.append(left)
        for i in range(len(height)-2,-1,-1):
            if height[i]> right:
                right_max[i] = height[i]
                right = height[i]
            else:
                right_max[i] = right
        for i in range(0,len(height)):
            result.append(min(left_max[i],right_max[i]))
        answer = 0

        for i in range(0,len(height)):
            answer+=result[i]-height[i]
        
        # print(left_max)
        # print(right_max)
        # print(result)

        return answer

