class Solution:
    def __init__(self):
        self.num_list = []
        self.Map = {}
        self.res = None
        
    def visit(self, visited_list, unvisited_list):
        print(visited_list, ":", unvisited_list)
        if(self.res != None):
            return
        if(len(unvisited_list) == 0):
            self.res = visited_list
            return
        
        this_node = visited_list[-1]
        adj = self.Map[this_node]
        for node in adj:
            if(node in unvisited_list):
                new_visited_list = visited_list[:]
                new_visited_list.append(node)
                new_unvisited_list = unvisited_list.copy()
                new_unvisited_list.remove(node)
                self.visit(new_visited_list,new_unvisited_list)
                


        
    def grayCode(self, n):
        if(n <= 0):
            return [0]
 
        for i in range(2**n):
            b = bin(i)[2:]
            b = "0"*(n-len(b)) + b
            self.num_list.append(b)
            
        D = {"0":"1", "1":"0"}
        for b in self.num_list:
            adj = []
            for i in range(len(b)):
                a = b[:i] + D[b[i]] + b[i+1:]
                adj.append(a)
            self.Map[b] = adj
            #print(b,":",adj)

        visited_list = [self.num_list[0]]
        unvisited_list = set(self.num_list[1:])
        self.visit(visited_list, unvisited_list)

        res = []
        for i in self.res:
            num = int(i, base = 2)
            res.append(num)
        return res



sol =  Solution()
print(sol.grayCode(2))
        

        
            
        
