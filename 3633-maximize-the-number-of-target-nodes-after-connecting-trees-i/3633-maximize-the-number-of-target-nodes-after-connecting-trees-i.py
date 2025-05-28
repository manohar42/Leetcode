class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        
        def Tree(edges):
            n = len(edges)+1
            tree = [[] for _ in range(n)]
            for i in edges:
                tree[i[0]].append(i[1])
                tree[i[1]].append(i[0])
            return tree
        tree1 = Tree(edges1)
        tree2 = Tree(edges2)
        max_connections = []
        
        def traverse(node,parent,tree,v):
            if v < 0:
                return 0
            res = 1
            for j in tree[node]:
                if j == parent:
                    continue
                res += traverse(j,node,tree,v-1)
            return res

        max_target_value = 0
        n = len(tree1)
        m = len(tree2)
        max_value = 0
        for i in range(n):
            targets = traverse(i,-1,tree1,k)
            max_connections.append(targets)
            
        for i in range(m):
            
            targets = traverse(i,-1,tree2,k-1)
            max_value = max(targets,max_value)


        return [i+max_value for i in max_connections]
