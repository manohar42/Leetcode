class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        free_days = 0
        previous_end_day = 0

        for start,end in meetings:

            if start > previous_end_day+1:
                free_days +=(start-previous_end_day-1)
            previous_end_day=max(end,previous_end_day)
        free_days+=(days-previous_end_day)
        return free_days