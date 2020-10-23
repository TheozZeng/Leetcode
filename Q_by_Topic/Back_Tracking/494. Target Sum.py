class Solution:
    def __init__(self):
        self.count = 0
        self.nums = []
        self.tar = None
        self.history = {0:1}
            
        
    def findTargetSumWays(self, nums, S: int) -> int:
        self.nums = nums
        self.tar = S
        for i in range(len(nums)):
            val = self.nums[i]
            #print(self.history)
            
            new_history = {}
            for prev_sum in self.history:
                count = self.history[prev_sum]                
                sum1 = prev_sum + val
                sum2 = prev_sum - val
                if(sum1 in new_history):
                    new_history[sum1] += count
                else:
                    new_history[sum1] = count
                if(sum2 in new_history):
                    new_history[sum2] += count
                else:
                    new_history[sum2] = count                
 
                    
            self.history = new_history
            
        #print(self.history)
        if(self.tar in self.history):
            return self.history[self.tar]
        return 0
        

sol = Solution()
nums = [1,1,1,1,1]
S = 3
print(sol.findTargetSumWays(nums, S))
