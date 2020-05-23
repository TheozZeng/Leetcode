class Solution:
    def generate(self, numRows: int):
        if(numRows == 0):
            return []
        if(numRows == 1):
            return[[1]]
        if(numRows == 2):
            return[[1],[1,1]]
        else:
            row = 3
            last_line = [1,1]
            triangle =  [[1],[1,1]]
            
            while(row <= numRows):
                L = [1]
                for i in range(0,len(last_line)-1):
                    L .append(last_line[i]+last_line[i+1])
                L.append(1)
                last_line = L
                triangle.append(L)
                row+=1
                
            return triangle

sol = Solution();
print(sol.generate(9))
        
