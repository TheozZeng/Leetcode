#subset for each num taking and not taking
#2**n sol

class Solution:
    def __init__(self):
        self.L = []
        
    def back_tracking(self, nums, L):
        if(len(nums)==0):
            self.L.append(L)
            return

        self.back_tracking(nums[1:], L)    
        self.back_tracking(nums[1:], L+[nums[0]])
        
            
    def subsets(self, nums) :
        if(len(nums)==0):
            return []
        self.back_tracking(nums, [])
        return self.L


nums = [1,2,3,4]
sol = Solution()
print(sol.subsets(nums))

