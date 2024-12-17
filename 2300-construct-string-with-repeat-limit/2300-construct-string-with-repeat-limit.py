class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        stack = []
        dic ={}
        for i in s:
            dic[i] = dic.get(i,0)+1
        heapq.heapify(stack)
        # print(dic)
        for i in dic:
            heapq.heappush(stack,(-ord(i),dic[i]))
        output = ""
        while stack:
            value,count = heapq.heappop(stack)
            s_1 = chr(-value)*min(count,repeatLimit)
            output+= s_1    
            count-=repeatLimit
            if count > 0 and stack:    
                ext_value,ext_count = heapq.heappop(stack)
                output+=chr(-ext_value)
                ext_count-=1
                if ext_count > 0:
                    heapq.heappush(stack,(ext_value,ext_count))
                heapq.heappush(stack,(value,count))

        return output


