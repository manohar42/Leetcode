class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        max_Water =0
        while left < right:
            area  = min(height[left],height[right])*(right-left)
            max_Water = max(max_Water,area)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_Water

