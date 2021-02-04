from Binary_tree import *
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

        self.tree_level = []
        # level order to find last complete level
        if(root == None):
            return
        this_level = [root]
        while(len(this_level)):
            self.tree_level.append(this_level)
            next_level = []
            for node in this_level:
                if(node.left):
                    next_level.append(node.left)
                if(node.right):
                    next_level.append(node.right)
            this_level = next_level
                    
        return
        

    def insert(self, v: int) -> int:
        if(self.root == None):
            self.root = TreeNode(v,None,None)
            self.tree_level.append([self.root])
            return
            
        n_level = len(self.tree_level)
        last_level = self.tree_level[-1]
        full_level_num = 2**(n_level-1)
        #last level is full
        if(len(last_level) == full_level_num):
            parent_node  = last_level[0]
            parent_node.left  = TreeNode(v,None,None)
            self.tree_level.append([parent_node.left])
            return parent_node.val
        
        #last level not full
        else:
            last_index = len(last_level) 
            parent_index = last_index//2
            parent_node = self.tree_level[-2][parent_index]
            is_right_child = last_index%2
            if(is_right_child == 0):
                parent_node.left = TreeNode(v,None,None)
                self.tree_level[-1].append(parent_node.left)
                return parent_node.val
            else: 
                parent_node.right = TreeNode(v,None,None)
                self.tree_level[-1].append(parent_node.right)
                return parent_node.val                 
        return
        

    def get_root(self) -> TreeNode:
        return self.root

    def print_level(self):
        for level in self.tree_level:
            for node in level:
                print(node.val,end = "-")
            print("")

T = [
[1],
[2,3],
[4,5,6,7],
[8,9,10,11,12,13,14,15],
[16,17]
]

root = build_Tree(T)
CBT = CBTInserter(root)
print(levelOrderBottom(CBT.get_root()))
CBT.print_level()

for i in range(18,1000):
    CBT.insert(i)

print(levelOrderBottom(CBT.get_root()))
CBT.print_level()
    

