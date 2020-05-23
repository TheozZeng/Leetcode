class Solution:
    def __init__(self):
        self.L = []
        
    def back_tracking(self, nums, L):
        if(len(nums)==0):
            self.L.append(L)
            return
            
        for num in nums:
            new_nums = []
            new_nums[:]= nums
            new_nums.remove(num)
            self.back_tracking(new_nums, L+[num])
            
    def permute(self, nums) :
        if(len(nums)==0):
            return []
        self.back_tracking(nums, [])
        return self.L


nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))

