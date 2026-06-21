class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = []
        max_area = 0

        for i in range(0,len(heights)):
            index = i
            while len(stack) > 0 and stack[-1][1] > heights[i]:
                index = stack[-1][0]
                area = (i-index)*stack[-1][1]
                max_area = max(area,max_area)
                stack.pop()
            
            stack.append((index, heights[i]))
        
        while len(stack) > 0:
            index = stack[-1][0]
            area = (len(heights)-index)*stack[-1][1]
            max_area = max(area,max_area)
            stack.pop()
        return max_area