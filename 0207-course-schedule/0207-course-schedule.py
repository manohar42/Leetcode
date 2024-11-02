class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if prerequisites ==[]:
            return True
        

        def dfs(i):
            if state[i] == 2:
                return True
            if state[i] == 1:
                return False
            state[i] = 1

            for j in graph[i]:
                if not dfs(j):
                    return False
            state[i] = 2
            return True


        graph = defaultdict(list)
        # print(graph)
        for i in prerequisites:
            graph[i[0]].append(i[1])
        # print(graph)
        
        state = [0 for _ in range(numCourses)]
        
        for i in range(0,numCourses):
            if not dfs(i):
                return False
        return True
                



