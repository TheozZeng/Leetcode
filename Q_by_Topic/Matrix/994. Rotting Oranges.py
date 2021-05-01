class Solution:
    def __init__(self):
        self.grid = []
        self.n_r =0
        self.n_c = 0
        self.res = 0
        self.finished = True

    def init_grid(self,grid):
        self.n_r = len(grid)
        self.n_c = len(grid[0])

        for r in range(self.n_r):
            this_row = []
            for c in range(self.n_c):
                val = grid[r][c]
                this_row.append(val)
                if(val == 1):
                    self.finished = False
            self.grid.append(this_row)
        
        
    def one_minute_passed(self):
        states_have_diff = False
        states_have_fresh = False
        new_grid = []
        
        for r in range(self.n_r):
            new_row = []
            for c in range(self.n_c):
                past_state = self.grid[r][c]
                now_state = past_state
                # find a fresh 
                if(past_state == 1):
                    top ,left ,right,down = False, False, False, False
                    if(r-1>=0):
                        top = (self.grid[r-1][c]== 2)
                    if(c-1>=0):
                        left = (self.grid[r][c-1] == 2)                    
                    if(r+1< self.n_r):
                        down = (self.grid[r+1][c] == 2)                        
                    if(c+1< self.n_c):
                        right = (self.grid[r][c+1] == 2)
                    # orange rot    
                    if(top or left or right or down):
                        now_state = 2
                        states_have_diff = True
                    # still have fresh
                    else:
                        states_have_fresh = True
                #update grid
                new_row.append(now_state)
            new_grid.append(new_row)
        self.grid = new_grid

        # 1 min passed
        self.res += 1
        # impossible 
        if(not states_have_diff and states_have_fresh):
            self.res = -1
            self.finished = True
            return
        # all rotten
        if (not states_have_fresh):
            self.finished = True
            return
        # need more time
        
                            
                

    def print_grid(self):
        print("time =", self.res, "min")
        for row in self.grid:
            print(row)
            
    def orangesRotting(self, grid):
        self.init_grid(grid)
        self.print_grid()
        while(not self.finished):
            self.one_minute_passed()
            self.print_grid()
            

grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution()
sol.orangesRotting(grid)
