class Solution:
    def maxProfit(self, prices) -> int:
        
        prev_A = None
        prev_B = None
        prev_C = None
        
        for p in prices:
            if(prev_A == None):
                A = 0
            else:
                A = max(prev_A,prev_C)
            
            if(prev_B == None):
                B = -p
            else:
                B = max(prev_A - p, prev_B)
            
            if(prev_C == None):
                C = 0
            else:
                C = prev_B + p

            prev_A = A
            prev_B = B
            prev_C = C
                
            #print(A,B,C)
            
        return max(A,B,C)


prices = [1,2,3,0,2]
sol = Solution()
print(sol.maxProfit(prices))
            
