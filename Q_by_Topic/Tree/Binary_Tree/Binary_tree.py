# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#-----------------------------------------------------------
def print_level(L):
    for node in L:
        if(node):
            print(node.val, end= "  ")
        else:
            print("*", end= "  ")
    print("")
    
def build_Tree(T):
    root = None
    prev_level = []
    for l in range(0,len(T)):
        '''
        print("level:",l,"--------------")
        print("prev_level->:",end="  ")
        print_level(prev_level)
        '''
        
        this_level = []
        for i in range(0,len(T[l])):
            if(T[l][i]):
                node = TreeNode()
                node.val = T[l][i]
            else:
                node = None
            this_level.append(node)

            prev_index = i //2
            #connect to prev level
            if(l==0):
                root = node                
            else:
                prevnode = prev_level[prev_index]
                if(i%2==0 and prevnode != None):
                    prevnode.left = node
                    '''
                    if(node):
                        print(prevnode.val,"->left",node.val)
                    else:
                        print(prevnode.val,"->left","None")
                    '''
                if(i%2==1 and prevnode != None):
                    prevnode.right = node
                    '''
                    if(node):
                        print(prevnode.val,"->right",node.val)
                    else:
                        print(prevnode.val,"->right","None")
                    '''
        prev_level = this_level

        '''
        print("this_level->:",end="  ")
        print_level(this_level)
        '''
    return root


def levelOrderBottom(root: TreeNode):
    #print("__________________________________")
    if(root == None):
        return []
    res = []
    this_level =[root]
    
    while(len(this_level)>0):
        '''
        print("level->:",end="  ")
        print_level(this_level)
        '''
        next_level =[]
        this_list = []
        for i in this_level:
            this_list.append(i.val)
            if(i.left):
                next_level.append(i.left)
            if(i.right):
                next_level.append(i.right)
        this_level = next_level
        res.append(this_list)
    return res


'''
T = [
[1],
[2.0,2.1],
[3.0,3.1,3.2,None],
[4.0,4.1,None,4.3,4.4,4.5,None,None]
]

root = build_Tree(T)
print(levelOrderBottom(root))
'''            
            
            
    
