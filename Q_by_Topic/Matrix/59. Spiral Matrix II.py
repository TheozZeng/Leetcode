class Solution:
    def __init__(self):
        self.res = None
        self.M = []
        self.n = None
        self.i = 1

    def print_M(self):
        for row in self.M:
            print(row)

    def init_matrix(self,n):
        self.n = n
        for r in range(n):
            row = []
            for c in range(n):
                row.append(None)
            self.M.append(row)
                
            
        
    def visit(self,ro,co, direction):
        self.print_M()
        print(ro,co)
        if(ro<0 or co<0 or ro>=self.n or co>=self.n ):
            return
        elif(self.M[ro][co] != None):
            return
        
        if(direction == "r"):
            for c in range(co,self.n+1):
                print(c)
                if(c == self.n):
                    break
                elif(self.M[ro][c] == None):
                    self.M[ro][c] = self.i
                    self.i += 1
                else:
                    break    
            self.visit(ro+1,c-1,"d")
            

        if(direction == "d"):
            for r in range(ro,self.n+1):
                if(r == self.n):
                    break
                if(self.M[r][co] == None):
                    self.M[r][co] = self.i
                    self.i += 1
                else:
                    break
            self.visit(r-1,co-1,"l")
            

        if(direction == "l"):
            for c in range(co,-2,-1):
                if(c == -1):
                    break
                if(self.M[ro][c] == None):
                    self.M[ro][c] = self.i
                    self.i += 1
                else:
                    break
            self.visit(ro-1,c+1,"u")                     

        if(direction == "u"):
            for r in range(ro,-2,-1):
                if(r == -1):
                    break
                if(self.M[r][co] == None):
                    self.M[r][co] = self.i
                    self.i += 1
                else:
                    break
            self.visit(r+1,co+1,"r")                   
            
        
        
        
    def generateMatrix(self, n):
        self.init_matrix(n)
        self.visit(0,0, "r")
        return self.M
        

n = 10      
sol = Solution()
print(sol.generateMatrix(n))
