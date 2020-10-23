class Solution:
    def __init__(self):
        self.sum = {0}
        
                
        
    def canPartition(self, nums) -> bool:
        if(sum(nums)%2 != 0):
            return False
        
        tar = sum(nums)//2
        for n in nums:
            #print(n, ":", self.sum)
            
            if((tar - n) in self.sum):
                return True
            
            new_sum = set()
            for s in self.sum:
                new_sum.add(s + n)
            self.sum = self.sum.union(new_sum)

        return False
                
            


nums = [1,5,11,5]
sol = Solution()
print(sol.canPartition(nums))
