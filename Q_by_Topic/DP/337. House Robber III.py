# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.max_val = 0
        self.left = left
        self.right = right


class Solution:
    def get_sum_of_children(self, node):
        num = 0
        if(node == None):
            return 0
        if(node.left != None):
            num += node.left.max_val
        if(node.right != None):
            num += node.right.max_val
        return num
            
    def get_max_val_at_node(self,root):
        if(root == None):
            return 0
        
        # can either rob the node children
        num1 =  self.get_sum_of_children(root) 
        
        # can rob itself and grandchildren
        left_sum  = self.get_sum_of_children(root.left)
        right_sum  = self.get_sum_of_children(root.right)
        num2 = root.val + left_sum + right_sum
        
        if(num1 > num2):
            root.max_val = num1
        else:
            root.max_val = num2
            
    def pre_order_traverse(self,node):
        if(node == None):
            return
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)
        self.get_max_val_at_node(node)
                
    def rob(self, root: TreeNode) -> int:
        self.pre_order_traverse(root)
        if(root == None):
            return 0
        return root.max_val
