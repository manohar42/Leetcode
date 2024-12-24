# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        # self.count = 0
        # def count_swaps(array1):
        #     arr = array1[:]
        #     target_array = sorted(arr)
        #     n = len(arr)
        #     hashmap = {}
        #     for i in range(len(arr)):
        #         hashmap[target_array[i]] = i
        #     # print(hashmap)

            
        #     for i in range(n):
        #         if arr[i] != target_array[i]:
        #             # print(arr,i)
        #             # print(target_array)
        #             self.count+=1
                    
        #             k = arr[i]
        #             arr[i] = arr[hashmap[arr[i]]]
        #             # print(arr[i])
        #             arr[hashmap[k]] = k

        #             # print(arr,arr[hashmap[arr[i]]])
        #             print(arr,target_array)

            

            
        
        # queue = deque()
        # queue.append(root)

        # while queue:
        #     level_size = len(queue)
        #     arr = []
        #     for _ in range(level_size):
        #         node = queue.popleft()
        #         arr.append(node.val)
        #         if node.left:
                    
        #             queue.append(node.left)
        #         if node.right:
                    
        #             queue.append(node.right)
        #     count_swaps(arr)
        # return self.count
        def dfs(i, idx, viz):
            if viz[i]: return 0
            viz[i]=True
            j=idx[i]
            return 1+dfs(j, idx, viz)

        q=deque()
        q.append(root)
        swaps=0
        while q:
            qz=len(q)
            arr=[0]*qz
            for i in range(qz):
                node=q.popleft()
                arr[i]=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            idx=sorted(range(qz), key = lambda k : arr[k])

            viz=[False]*qz
            for i in range(qz):
                if not viz[i]:
                    swaps+=dfs(i, idx, viz)-1
        return swaps