class Solution:
    def __init__(self):
        self.prerequisites_list = {}
        self.Node_status = []
        # 0 -> unvisited
        # 1 -> processing
        # 2 -> processed
        self.has_cycle = False
        self.res = []

    def gen_prerequisites_list(self, prerequisites):
        for node_pair in prerequisites:
            pre = node_pair[1]
            now = node_pair[0]
            if(now in self.prerequisites_list):
                self.prerequisites_list[now].append(pre)
            else:
                self.prerequisites_list[now] = [pre]
                
    def DFS_find_order(self, node):
        print(node, "|", self.Node_status)
        if(self.has_cycle):
            return
        node_status = self.Node_status[node]
        
        if(node_status == 0):
            self.Node_status[node] = 1
            if(node in self.prerequisites_list):
                adj_node = self.prerequisites_list[node]
                for next_node in adj_node:
                    self.DFS_find_order(next_node)
            self.Node_status[node] = 2
            self.res.append(node)

        elif(node_status == 1):
            self.has_cycle = True
            return  

        elif(node_status == 2):
            return  
              
    def findOrder(self, numCourses, prerequisites):
        self.Node_status = numCourses * [0]
        self.gen_prerequisites_list(prerequisites)
        print(self.prerequisites_list)
        for i in range(numCourses):
            self.DFS_find_order(i)
        if(self.has_cycle):
            return []
        return self.res



sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses, prerequisites))
