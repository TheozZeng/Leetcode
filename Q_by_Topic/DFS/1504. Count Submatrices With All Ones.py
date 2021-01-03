class Solution:
    def __init__(self):
        self.mat = None
        self.n_r = 0
        self.n_c = 0 
        self.S = set()
        
    def find_sub_matrix_given(self,r1,c1,r2,c2):
        Sub1 = (r1,c1,r2,c2+1)
        if(Sub1 not in self.S):
            if(c2+1 < self.n_c):
                All_1 = True
                for r in range(r1,r2+1):
                    if(self.mat[r][c2+1] == 0):
                        All_1 = False
                        break
                if(All_1):
                    #print(Sub1)
                    self.S.add(Sub1)
                    self.find_sub_matrix_given(r1,c1,r2,c2+1)
                    
        Sub2 = (r1,c1,r2+1,c2)
        if(Sub2 not in self.S):
            if(r2+1 < self.n_r):
                All_1 = True
                for c in range(c1,c2+1):
                    if(self.mat[r2+1][c] == 0):
                        All_1 = False
                        break
                if(All_1):
                    #print(Sub2)
                    self.S.add(Sub2)
                    self.find_sub_matrix_given(r1,c1,r2+1,c2)
                    
        
                    
            
    def numSubmat(self, mat):
        self.mat = mat
        self.n_r = len(mat)
        self.n_c = len(mat[0])
        for r in range(self.n_r):
            for c in range(self.n_c):
                if(mat[r][c] == 1):
                    self.S.add((r,c,r,c))
                    self.find_sub_matrix_given(r,c,r,c)
        return len(self.S)

mat = [[1,1,1,1,0],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,0,0]]

sol = Solution()
print(sol.numSubmat(mat))
    




        
        
