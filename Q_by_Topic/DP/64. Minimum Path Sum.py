class Solution:
    def minPathSum(self, grid):
        num_row = len(grid)
        if(num_row == 0):
            return 0
        num_col = len(grid[0])
        if(num_col == 0):
            return 0
        res = num_row * [num_col * [None]]
        
        for row in range(num_row):
            for col in range(num_col):
                this_num = grid[row][col]
                if(row == 0 and col ==0):
                    res[row][col]= this_num
                elif(row == 0):
                    res[row][col]= this_num + res[row][col-1]
                elif(col == 0):
                    res[row][col]= this_num + res[row-1][col]
                else:
                    left = res[row][col-1]
                    top = res[row-1][col]
                    min_path = min(this_num + left, this_num + top)
                    res[row][col] = min_path
        return res[-1][-1]
                    
                
        





grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
sol = Solution()
print(sol.minPathSum(grid))
