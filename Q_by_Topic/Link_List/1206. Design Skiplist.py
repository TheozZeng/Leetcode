import random

class Node:
    def __init__(self, val = -float("inf")):
        self.val = val
        self.next = None
        self.up = None
        return
        
    def insert_after(self, num):
       new_node = Node(num)
       next_node = self.next
       new_node.next = next_node
       self.next = new_node
       return new_node

    def delete_after(self,num):
        node = self
        # found node to del
        if(node.next == None):
            return False
        if(node.next.val == num):
            node.next = node.next.next
            return True
        return False

    def find_in_level(self,num):
        node = self
        while(node.next != None):
            if(node.next.val >= num):
                return node
            node = node.next
        return node

    def print_list(self):
        node = self.next
        while(node):
            print(node.val ,end = "->")
            node = node.next
        print("None")
        

head = Node()
for i in range(20,-1,-1):
    head.insert_after(i)
'''    
head.print_list()
node = head.find_in_level(14)
print(id(node), node.val )
node.delete_after(14)
head.print_list()
'''          
            

class Skiplist:
    def __init__(self):
        level_0 = Node() 
        self.Skip_L = [level_0]

    def print_Skiplist(self):
        for node in self.Skip_L:
            node.print_list()
        print("_____________________________________")

    def find(self,tar):
        L = []
        tot_level  = len(self.Skip_L) -1
        level = tot_level
        while(level >= 0):
            if(level == tot_level):
                node = self.Skip_L[level]
            prev = node.find_in_level(tar)
            print("level =", level)
            node.print_list()
            print("prev.val = ", prev.val)
            node = prev.up
            level -= 1
            L.append(prev)
        return L
            
    def search(self, target: int) -> bool:
        level_list = self.find(target)
        prev = level_list[-1]
        if(prev.next == None):
            return False
        elif(prev.next.val == target):
            return True
        return False
        

    def add(self, num: int) -> None:
        level_list = self.find(num)
        level_list.reverse()
        up_node = None
        for i in range(len(level_list)):
            # add to this level
            prev = level_list[i]
            this_node  = prev.insert_after(num)
            # up_node connect to this node
            this_node.up = up_node
            up_node = this_node
            # random to continue
            if(random.randint(0,1) > 0):
                return
            
        # add new level
        if(random.randint(0,1) > 0):
            prev_head = self.Skip_L[-1]
            this_head = Node()
            this_head.up = prev_head
            this_node = this_head.insert_after(num)
            this_node.up = up_node
            self.Skip_L .append(this_head)
           
        return


    def erase(self, num: int) -> bool:
        level_list = self.find(num)
        prev = level_list[-1]
        if(prev.next == None):
            return False
        elif(prev.next.val != num):
            return False

        for prev in level_list:
            prev.delete_after(num)
        return True

sol = Skiplist()
L = [8,9,2,5,1,9,3,6,7,2,2,2,4,4]
for i in L:
    print("add: ",i)
    sol.add(i)
    sol.print_Skiplist()

L = [8,9,2,5,1,9]
for i in L:
    print("erase:",i)
    sol.erase(i)
    sol.print_Skiplist()
    
  
