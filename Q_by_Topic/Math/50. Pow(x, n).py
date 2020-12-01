class Solution:
    def __init__(self):
        self.x = None
        self.n = None
        self.res = None
        
    def find_Pow(self,base, base_power):
        res = base
        if(base_power == self.n):
            self.res = res
            return            
        
        new_power = 1
        new_base = self.x    
        while((base_power + new_power*2) <= self.n):
            res = base * new_base
            print(base_power,"|",new_power,"|",res)
            new_power *= 2
            new_base *= new_base

        res = base * new_base  
        print(base_power,"|",new_power,"|",res)    
        if(base_power + new_power == self.n):
            self.res = res
            return
        print("_______________________________")
        self.find_Pow(res,base_power + new_power)

        
    def myPow(self, x: float, n: int) -> float:
        self.x = x
        if(n >= 0):
            self.n = n
            self.find_Pow(1,0)
            return float(self.res)
        else:
            self.n = -n
            self.find_Pow(1,0)
            return 1.0/self.res

sol = Solution()
print(sol.myPow(3,0))
