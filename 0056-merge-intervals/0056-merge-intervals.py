class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        n = len(intervals)

        s= [sorted_intervals[0]]

        for i in sorted_intervals[1:]:

            if s[-1][1] >= i[0]:
                k = [min(s[-1][0], i[0]), max(i[1],s[-1][1])]
                s.pop()
                s.append(k)
            else:
                s.append(i)
        return s
