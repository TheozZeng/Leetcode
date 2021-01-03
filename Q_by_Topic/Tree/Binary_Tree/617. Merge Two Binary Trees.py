# 617. Merge Two Binary Trees
from Binary_tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if(t1 == None and t2 == None):
            return None
        
        this_node = TreeNode()
        if(t1 == None):
            this_node.val = t2.val
            left_node = self.mergeTrees(t2.left, None)
            right_node = self.mergeTrees(t2.right, None)
            
        elif(t2 == None):
            this_node.val = t1.val
            left_node = self.mergeTrees(t1.left, None)
            right_node = self.mergeTrees(t1.right, None)
            
        else:
            this_node.val = t1.val + t2.val
            left_node = self.mergeTrees(t1.left, t2.left)
            right_node = self.mergeTrees(t1.right, t2.right)
           
        this_node.left = left_node
        this_node.right = right_node
        return this_node
