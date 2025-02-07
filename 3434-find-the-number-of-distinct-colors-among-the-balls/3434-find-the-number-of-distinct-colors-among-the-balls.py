class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        color_map = {}
        ball_map = {}
        result = []
        for x,y in queries:

            if x in ball_map:
                previous_color = ball_map[x]
                color_map[previous_color]-=1
                
                if color_map[previous_color] == 0:
                    del color_map[previous_color]
            color_map[y] = color_map.get(y,0)+1
            ball_map[x] = y
            result.append(len(color_map))
        return result
                            