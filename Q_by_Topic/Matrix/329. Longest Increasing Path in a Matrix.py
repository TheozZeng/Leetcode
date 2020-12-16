class Solution:
    def __init__(self):
        self.matrix = None
        # path len from this node
        self.matrix_path = []
        self.n_r = None
        self.n_c = None
        self.longest = 0
        
    def DFS(self,r,c,prev_val):
        # out of range
        if(r<0 or c<0 or r>= self.n_r or c>= self.n_c):
            return 0
        # not increasing
        this_val = self.matrix[r][c]
        if(prev_val >= this_val):
            return 0
        # already visited
        if(self.matrix_path[r][c] != None):
            return self.matrix_path[r][c]

        up = self.DFS(r-1,c,this_val)
        down = self.DFS(r+1,c,this_val)
        left  = self.DFS(r,c-1,this_val)
        right = self.DFS(r,c+1,this_val)
        res = max(up,down,left,right) + 1
        self.matrix_path[r][c] = res
        #self.print_matrix(self.matrix_path)
        self.longest = max(self.longest,res)
        return res
        
        
            
    def print_matrix(self,matrix):
        for row in matrix:
            print(row)
        print("____________________")
            
    def longestIncreasingPath(self, matrix) -> int:
        self.matrix = matrix
        self.n_r = len(matrix)
        if(self.n_r == 0):
            return 0
        self.n_c = len(matrix[0])
        for r in range(self.n_r):
            row = []
            for c in range(self.n_c):
                row.append(None)
            self.matrix_path.append(row)
        
        for r in range(self.n_r):
            for c in range(self.n_c):
                self.DFS(r,c,-float("inf"))
        return self.longest
