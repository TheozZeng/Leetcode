# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if(len(preorder) == 0):
            return None

        root_val = preorder.pop(0)
        root = TreeNode()
        root.val = root_val
        print(root_val,":",preorder,"|",inorder)
        
        index_val = inorder.index(root_val)
        left_inorder = inorder[:index_val]
        right_inorder = inorder[index_val+1:]
        
        size_left_tree = len(left_inorder)        
        left_preorder = preorder[:len(left_inorder)]
        right_preorder = preorder[len(left_inorder):]
       
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
sol.buildTree(preorder, inorder)

