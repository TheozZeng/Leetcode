class Node:
    def __init__(self,val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
        self.size_left_tree = 0
        
class Solution:
    def __init__(self):
        self.root = None
        
    def insert_BST(self,this_node,val):
        
        #initial root
        if(self.root == None):
            new_node = Node(val)
            self.root = new_node
            return
        
        if(this_node.val == val):
            this_node.count += 1
            return

        if(val < this_node.val):
            if(this_node.left == None):
                new_node = Node(val)
                this_node.left = new_node
            else:
                self.insert_BST(this_node.left, val)

        elif(val > this_node.val):
            if(this_node.right == None):
                new_node = Node(val)
                this_node.right = new_node
            else:
                self.insert_BST(this_node.right, val)

    def inorder_traverse(self, node):
        if(node == None):
            return
        self.inorder_traverse(node.left)
        print(node.val, end = "->")
        self.inorder_traverse(node.right)
            
    
    def countSmaller(self, nums):
        for i in range(len(nums)-1,-1,-1):
            self.insert_BST(self.root,nums[i])
        self.inorder_traverse(self.root)

nums = [10,9,8,34,1,6,7,3,24,6,3,3,45,0]
sol = Solution()
sol.countSmaller(nums)
print(sorted(nums))
            
        
