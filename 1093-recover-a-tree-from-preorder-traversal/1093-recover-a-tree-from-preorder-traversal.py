# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        

        hashmap = {}
        n = len(traversal)
        i = 0
        s= ""
        while i < n and traversal[i]!= "-":
            s+=traversal[i]
            i+=1
        # print(s)
        hashmap[0] = TreeNode(int(s))
        # print(hashmap[0])
        count = 0
        while i < n:
            # print(i,count)
            if traversal[i] == '-':
                count+=1
                i+=1
                continue
            else:
                s = ""
                while i < n and traversal[i]!= '-' :
                    s+=traversal[i]
                    i+=1
                # print("s",s)
                s = int(s)
                # print("Int",s)
                hashmap[count] = TreeNode(s)
                if hashmap[count-1].left == None:
                    hashmap[count-1].left = hashmap[count]
                else:
                    hashmap[count-1].right = hashmap[count]
                # i+=1
                count = 0
        # for i in hashmap:
        #     print(hashmap[i])
        #     print("    ")
        return hashmap[0]


