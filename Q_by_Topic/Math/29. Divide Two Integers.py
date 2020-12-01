class Solution:
    def __init__(self):
        self.divisor = None
        self.dividend = None
        self.res = None
        
    def find_num_with_start(self, base, res):
        if(base + self.divisor > self.dividend):
            self.res = res
            return
        
        p = 0
        pow_2 = self.divisor
        # pow_2 = divisor*2**p
        #print("----------------------------------")
        while (base +  2 * pow_2 <= self.dividend):
            pow_2 += pow_2
            p += 1
            #print(base , p , base + pow_2)

        new_base = base + pow_2
        new_res = res + 2**p
        self.find_num_with_start(new_base, new_res)

            
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend == 0):
            return 0

        # solve the problem of sign + -
        positive = False        
        if(dividend >0 and divisor >0) or (dividend <0 and divisor<0):
            positive = True

        self.divisor = abs(divisor)
        self.dividend = abs(dividend)

        # find the num range
        self.find_num_with_start(0,0)
        
        
        
        if(not positive):
            self.res = -self.res
        return min(max(self.res,-(2**31-1)), 2**31-1)


dividend = -2147483648
divisor = -1
sol = Solution()
print(sol.divide(dividend, divisor))
