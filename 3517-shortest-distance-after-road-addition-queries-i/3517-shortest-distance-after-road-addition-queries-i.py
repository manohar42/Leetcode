class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def shortestpath(graph,start,end):
            
            queue = deque()
            queue.append((start,0))
            visited = set()
            length = 0
            while queue:
                k,length = queue.popleft()
                if k == end:
                    return length
                visited.add(k)
                for i in graph[k]:
                    if i not in visited:
                        queue.append((i,length+1))  

        graph = defaultdict(list)
        

        for i in range(1,n):
            graph[i-1].append(i)
        res = []
        for i in queries:
            graph[i[0]].append(i[1])
            # print(graph)
            # visited = [False]*n
            k = shortestpath(graph,0,n-1)
            res.append(k)
        return res