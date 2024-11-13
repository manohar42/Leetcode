class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        queue = deque([source])
        visited = [False for _ in range(n)]
        
        while queue:   
            # print(queue)
            k = queue.pop()
            
            for i in d[k]:
                if i ==  destination:
                    return True
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False
        
