# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        mid_val = root.val
        lis = []
        
        def  checkBST(root):
            if root is None:
                return 
            checkBST(root.left)
            lis.append(root.val)
            checkBST(root.right)
        
        
        checkBST(root)
        for i in range(1,len(lis)):
            if lis[i] <= lis[i-1]:
                return False

        return True