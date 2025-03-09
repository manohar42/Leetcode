class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        n= len(colors)
        colors = colors+colors[:k-1]
        n = len(colors)
        count = 0
        group_count = 0
        for i in range(1,n):
            if colors[i] != colors[i-1]:
                count+=1
            else:
                count = 0
            if count >= k-1:
                group_count+=1
        return group_count
            
