class Solution:
    def minCost(self, s, cost):
        prev_c = None
        res = 0
        
        L = []
        for i in range(len(s)):
            this_c = s[i]
            this_cost = cost[i]
            
            if(this_c != prev_c and prev_c != None):
                prev_max = max(L)
                prev_sum = sum(L)
                res += (prev_sum - prev_max)
                L = []
            L.append(this_cost)
            #print(this_c,":",L,":",res)
            prev_c = this_c
            
        if(L):
            prev_max = max(L)
            prev_sum = sum(L)
            res += (prev_sum - prev_max)
            
        return res
            
        
        



s = "aaabbbabbbb"
cost = [3,5,10,7,5,3,5,5,4,8,1]
sol = Solution()
print(sol.minCost( s , cost))
