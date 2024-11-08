# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def subTreeCheck(root,subRoot):
            
            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False
            
            if root.val == subRoot.val:
                return subTreeCheck(root.left,subRoot.left) and subTreeCheck(root.right,subRoot.right)
            return False

        def check(root,subRoot):
            # if root is None and subRoot is None:
            #     return False
            if root is None or subRoot is None:
                return False
            value = False
            if root.val == subRoot.val:
                value = subTreeCheck(root.right,subRoot.right) and subTreeCheck(root.left, subRoot.left)
            if value == False:
                return check(root.right, subRoot) or check(root.left,subRoot)
            else:
                return True
            
        return check(root,subRoot)


            