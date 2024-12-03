# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def createTree(start,end):
            res = []
            if start > end:
                res.append(None)
                return res 

            for i in range(start,end+1):
                left_tree = createTree(start,i-1)
                right_tree = createTree(i+1,end)
                
                for j in left_tree:
                    for k in right_tree:
                        tree = TreeNode(i,j,k)
                        res.append(tree)
            
            return res[:]
        return createTree(1,n)



