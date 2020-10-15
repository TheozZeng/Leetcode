class Solution:
    def __init__(self):
        self.square_list = []
        self.processed = []
    

        
    def min_square_for_tar(self, tar):
                   
        for i in self.square_list:
            new_tar = tar - i
            if(new_tar <0):
                continue
            elif(new_tar == 0):
                self.processed[tar] = 1
            else:
                val = self.processed[new_tar]
                self.processed[tar] = min(self.processed[tar], val+1)
        #print(self.processed)
            
        
    def numSquares(self, n: int) -> int:      
        i = 1
        while(i**2 <= n):
            self.square_list.append(i**2)
            i+=1
        self.square_list.reverse()
        print(self.square_list)

        self.processed = (n+1) * [float("inf")]
        for i in range(1,n+1):
            self.min_square_for_tar(i)
        return self.processed[n]



        for i in range(1,n+1):
            self.min_square_for_tar(i)
        return self.processed[n]







