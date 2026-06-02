class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        res = float('inf')
        for i in range(0,len(landStartTime)):
            time_taken=landStartTime[i]+landDuration[i]
            for j in range(0,len(waterStartTime)):
                if waterStartTime[j] >= time_taken:
                    time_taken=waterStartTime[j]+waterDuration[j]
                else:
                    time_taken+=waterDuration[j]

                if time_taken < res:
                    res = time_taken
                time_taken=landStartTime[i]+landDuration[i]
        for i in range(0,len(waterStartTime)):
            time_taken =waterStartTime[i]+waterDuration[i]
            for j in range(0,len(landStartTime)):
                if landStartTime[j] >= time_taken:
                    time_taken=landStartTime[j]+landDuration[j]
                else:
                    time_taken +=landDuration[j]
                if time_taken < res:
                    res = time_taken
                time_taken=waterStartTime[i]+waterDuration[i]

        return res