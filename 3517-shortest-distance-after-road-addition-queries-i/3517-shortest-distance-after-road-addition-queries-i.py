class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(1,n):
            graph[i-1].append(i)

        def shortestpath(graph,start,end): 
            queue = deque()
            queue.append((start,0))
            visited = set()
            while queue:
                k,length = queue.popleft()
                if k == end:
                    return length
                visited.add(k)
                for i in graph[k]:
                    if i not in visited:
                        queue.append((i,length+1))  

        res = []
        for i in queries:
            graph[i[0]].append(i[1])
            k = shortestpath(graph,0,n-1)
            res.append(k)
        return res