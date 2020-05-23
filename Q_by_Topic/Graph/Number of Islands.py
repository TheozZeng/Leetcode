class Solution:
    def __init__(self):
        self.L = None
        self.count = 0
        
    def DFS(self,i,j,visited):
        #first DFS around then mark as *
        
        if(i in range(0,len(self.L)) and j in range(0,len(self.L[0]))):
            if(self.L[i][j] != "1"):
                return
            
            if(self.L[i][j] == "1" and visited == False):
                self.count += 1
                visited = True
            
            #mark as visited
            self.L[i][j] = "*"
            
            self.DFS(i-1,j,visited)
            self.DFS(i+1,j,visited)
            self.DFS(i,j-1,visited)
            self.DFS(i,j+1,visited)
            
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.L = grid
        for i in range(len(self.L)):
            for j in range(len(self.L[0])):
                self.DFS(i,j,False)
        return self.count
