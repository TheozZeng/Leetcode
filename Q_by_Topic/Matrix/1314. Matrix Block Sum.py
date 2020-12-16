class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        L = []
        # init 0 matrix
        for r in range(len(mat)):
            row = []
            for c in range(len(mat[0])):
                row.append(0)
            L.append(row)
            
            
        # L[i][j] = sum mat[:i][:j]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if(c == 0):
                    L[r][c] = mat[r][c]
                else:
                    L[r][c] = mat[r][c] + L[r][c-1]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if(r != 0):
                    L[r][c] = L[r][c] + L[r-1][c]
        

        # calculate res
        res = []
        # init 0 matrix
        for r in range(len(mat)):
            row = []
            for c in range(len(mat[0])):
                row.append(0)
            res.append(row)
            
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                r1 = r-K-1
                c1 = c-K-1
                r2 = min(len(mat)-1, r+K)
                c2 = min(len(mat[0])-1,c+K)
                
                #Pa
                if(r1 < 0 or c1 <0):
                    Pa = 0
                else:
                    Pa = L[r1][c1]
                    
                #pb
                if(c1 < 0):
                    Pb = 0
                else:
                    Pb = L[r2][c1]
                
                #Pc
                if(r1 < 0):
                    Pc = 0
                else:
                    Pc = L[r1][c2]
                    
                #Pd
                Pd = L[r2][c2]
                
                res[r][c] = Pd - Pb -Pc + Pa
                
        return res
                
                
