class Solution:
    def __init__(self):
        self.n = 0
        self.res = []
        
    def generated_board(self,L):
        B = []
        for r in range(self.n):
            row = ""
            for c in range(self.n):
                if(c >= len(L)):
                    row = row + "  "
                elif(L[c] == r):
                    row = row + "X"
                else:
                    row = row + "O"
            B.append(row)
        return B
            
    def print_board(self,B):
        for row in B:
            print(row)
        print("--------------------------")
        
    def  add_Q(self,L):
        '''
         L  [1, 3, 0]
         ==>
         .    .    Q  ?
         Q  .     .   ?
         .    .     .   ?
         .    Q   .   ?
        '''
        #self.print_board(self.generated_board(L))
        if(len(L) == self.n):
            self.res.append(L)
            return
        
        x = len(L)
        for y in range(self.n):
            is_y_valid = True
            for xi in range(len(L)):
                yi = L[xi]
                dx = abs(x-xi)
                dy = abs(y-yi)
                if(dx == 0 or dy == 0 or dx == dy):
                    is_y_valid = False
                    break
            if(is_y_valid):
                self.add_Q(L + [y])
                    
                    
    def solveNQueens(self, n):
        self.n = n
        self.add_Q([])
        res = []
        for L in self.res:
            B = self.generated_board(L)
            self.print_board(B)
            res.append(B)
        return res
            
            
        
 
sol = Solution()
print(sol.solveNQueens(4))
