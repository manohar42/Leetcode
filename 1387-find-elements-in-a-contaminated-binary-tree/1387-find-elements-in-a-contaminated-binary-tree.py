# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:


    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.root = root
        if self.root.val != 0:
            self.root.val = 0
            self.values.add(root.val)
        self.setValues(self.root)
    def setValues(self, node):
        if node.left:
            node.left.val = 2*node.val+1
            self.values.add(node.left.val)
            self.setValues(node.left)
        if node.right:
            node.right.val = 2*node.val+2
            self.values.add(node.right.val)
            self.setValues(node.right)
    def traverse(self, node,target):
        if node is None:
            return False
        if node.val == target:
            return True
        else:
            return self.traverse(node.left,target) or self.traverse(node.right,target)
        

    def find(self, target: int) -> bool:
        return target in self.values
        # return self.traverse(self.root,target)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)