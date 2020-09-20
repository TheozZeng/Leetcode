from Binary_tree import *

class Solution:
    def Balanced_Node(self, node):
        if(node == None):
            return[True,0]
        else:
            left_res = self.Balanced_Node(node.left)
            right_res = self.Balanced_Node(node.right)
            if(left_res[0]==False or right_res[0]==False):
                return[False,None]
            else:
                if (abs(left_res[1]- right_res[1]) > 1):
                    return[False,None]
                else:
                    return[True, max(left_res[1],right_res[1])+1]
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.Balanced_Node(root)[0]

T = [
[1],
[2.0,2.1],
[3.0,3.1,3.2,3.3],
[4.0,4.1,None,4.3,4.4,4.5,None,None]
]

root = build_Tree(T)
sol = Solution()
print(sol.isBalanced(root))
