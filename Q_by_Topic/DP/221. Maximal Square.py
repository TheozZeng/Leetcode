class Solution:
    def maximalSquare(self, matrix):
        n_r = len(matrix)
        if(n_r == 0):
            return 0
        n_c = len(matrix[0])
        if(n_c == 0):
            return 0

        #!!!!! init 2D array
        DP = []
        for i in range(n_r):
            DP.append(n_c * [0])
            
        res = 0
        for r in range(n_r):
            for c in range(n_c):
                if(matrix[r][c] == "0"):
                    DP[r][c] = 0
                elif(r==0 or c==0):
                    DP[r][c] = 1
                else:
                    DP[r][c] = min(DP[r-1][c],DP[r][c-1],DP[r-1][c-1])+1
                res = max(res, DP[r][c])
        print_matrix(DP)
        return res**2
        
matrix = [["1","0","1","0","0"],
               ["1","0","1","1","1"],
               ["1","1","1","1","1"],
               ["1","0","0","1","0"]]

def print_matrix(matrix):
    for row in matrix:
        print(row)

print_matrix(matrix)        
sol = Solution()
print(sol.maximalSquare(matrix))
