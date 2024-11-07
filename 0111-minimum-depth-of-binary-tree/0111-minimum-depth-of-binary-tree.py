# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            
            if root is None:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            if left == 0 or right == 0 :
                return max(left,right)+1

            return min(left,right)+1
        
        return height(root)
