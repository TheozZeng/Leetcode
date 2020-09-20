from Binary_tree import *

class Solution:
    def __init__(self):
        self.count = 0
        self.tar = None

     #when DFS at a node, It check itself up the list   
    def DFS(self, L, node):
        if(node == None):
            return
        
        temp_sum = 0
        L.append(node.val)
        
        for i in L[::-1]:
            temp_sum += i
            if(temp_sum == self.tar):
                self.count += 1

        self.DFS(L[:],node.left)
        self.DFS(L[:],node.right)
            
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.tar = sum
        L = []
        self.DFS(L,root)
        return self.count

T = [
[10],
[5,-3],
[3,2,11,None],
[3,-2,None,1]
]

root = build_Tree(T)
sol = Solution()
print(sol.pathSum(root,8))
