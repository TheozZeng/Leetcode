class Solution:
    def countBits(self, num: int):
        dp = [0,1]
        
        pow_2_low = 1
        
        for i in range(2,num+1):
            if( i == 2** pow_2_low):
                print("__________________________________")
                pow_2_low += 1
                
            index = i-2**(pow_2_low-1)
            this_count = dp[index]+1
            print(i,":", pow_2_low,":",index,":",this_count)
            dp.append(this_count)
        return dp[0:num+1]

sol = Solution()
print(sol.countBits(20))
