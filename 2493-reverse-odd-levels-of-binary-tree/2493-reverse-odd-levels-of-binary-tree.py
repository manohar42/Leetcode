# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(rightchild,leftchild,level):

            if rightchild is None or leftchild is None:
                return
            if level%2 == 0:
                rightchild.val,leftchild.val = leftchild.val,rightchild.val
            dfs(rightchild.right,leftchild.left,level+1)
            dfs(rightchild.left,leftchild.right,level+1)
        dfs(root.right,root.left,0)
        return root
