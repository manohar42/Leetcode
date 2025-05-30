class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        n = len(edges)
        dist1 = [float('inf') for i in range(n)]
        dist2 = [float('inf') for i in range(n)]
        visit1 = [False]*n
        visit2 = [False]*n
        dist1[node1] = 0
        dist2[node2] = 0

        def dfs(node,dist,visit,edges):
            # print(visit)
            visit[node] = True
            neighbor = edges[node]
            if neighbor != -1 and not visit[neighbor]:
                dist[edges[node]] = 1+dist[node]
                dfs(edges[node],dist,visit,edges)

        dfs(node1,dist1,visit1,edges)
        dfs(node2,dist2,visit2,edges)
        # print(visit1)
        # print(visit2)
        # print(dist1)
        # print(dist2)

        minDistance = -1
        minDistanceTillnow = float('inf')

        for i in range(0,n):
            if minDistanceTillnow > max(dist1[i],dist2[i]):
                minDistanceTillnow = max(dist1[i],dist2[i])
                minDistance = i
        return minDistance

