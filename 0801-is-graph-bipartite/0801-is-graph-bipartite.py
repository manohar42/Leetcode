class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        visited = {}
        for i in range(len(graph)):
            visited[i] = False

        
        
        for i in range(len(graph)):
            if visited[i] != False:
                continue
            queue = deque()
            queue.append(i)
            visited[i] = "A"
            while queue:

                k = queue.pop()

                for i in graph[k]:
                    if visited[i] == False:
                        # print(visited[k])
                        visited[i] = "A" if visited[k] == "B" else "B"
                        queue.append(i)
                    if visited[i] == visited[k]:
                        # print(i,k)
                        # print(visited)
                        return False
        return True
