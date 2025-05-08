class State:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis


class Solution:
    def minTimeToReach(self, moveTime):

        m = len(moveTime[0])
        n = len(moveTime)
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        v = [[0 for i in range(0,m)] for j in range(0,n)]
        dis = [[float("inf")]*m for j in range(0,n)]
        dis[0][0] = 0
        q = []
        heapq.heapify(q)
        heapq.heappush(q,State(0,0,0))

        while q:
            val = heapq.heappop(q)
            if v[val.x][val.y]:
                continue
            v[val.x][val.y] =1
            for dx,dy in directions:
                i,j = val.x+dx,val.y+dy

                if not (0<=i<n and 0<=j<m):
                    continue
                dist = max(dis[val.x][val.y], moveTime[i][j])+1
                
                if dis[i][j] > dist:
                    dis[i][j] = dist
                    heapq.heappush(q,State(i,j,dist))
        # print(dis)
        return dis[n-1][m-1]