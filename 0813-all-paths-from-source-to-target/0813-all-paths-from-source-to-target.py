class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        start = 0
        end = len(graph)-1
        res = []
        def find_all_paths(current_node, path):

            if current_node == end:
                res.append(path[:])
                return
            for node in graph[current_node]:
                path.append(node)
                find_all_paths(node, path)
                path.pop()
        
        find_all_paths(0,[0])

        return res



            
        return find_all_paths(start,[])
        

        
