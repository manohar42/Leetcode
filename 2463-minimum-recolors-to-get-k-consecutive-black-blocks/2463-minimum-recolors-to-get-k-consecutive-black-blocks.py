class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        left = 0
        right = 0
        white_count = 0
        min_operations = float("inf")
        while right<k:
            if blocks[right] == "W":
                white_count+=1
            right+=1
        # print(white_count)
        min_operations = white_count
        while right < len(blocks):
            # print(white_count)
            if blocks[right] == "W":
                white_count+=1
            if blocks[left] == "W":
                white_count-=1
            min_operations = min(min_operations,white_count)
            right+=1
            left+=1
            # print(right,left)
        
        return min_operations
            
