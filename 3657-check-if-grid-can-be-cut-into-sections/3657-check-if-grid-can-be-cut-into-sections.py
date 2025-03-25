class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        

        def check(rectangle,axis):

            rectangle.sort(key = lambda x:x[axis])
            cuts = 0
            previous_end = rectangle[0][axis+2]
            for i in range(1,len(rectangle)):
                bar = rectangle[i]
                # print(bar[axis],previous_end)
                if bar[axis] >=previous_end:
                    cuts+=1
                previous_end = max(previous_end, bar[axis+2])
            print(cuts)
            return cuts>=2
        

        return check(rectangles,1) or check(rectangles,0)