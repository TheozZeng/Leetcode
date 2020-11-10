class Solution:
    def maxProduct(self, nums):
        if(len(nums) == 0):
            return -1
        
        cur_max = nums[0]
        cur_min = nums[0]
        res_max = nums[0]
        
        print(nums[0], "I", cur_max, "|",cur_min)
        for i in range(1,len(nums)):
            n = nums[i]
            temp_max = cur_max
            # find max min of subarray to index i
            cur_max = max(cur_max *n, cur_min*n, n)
            cur_min = min(temp_max *n, cur_min*n, n)
            res_max = max(res_max,cur_max)
            print(n, "|", cur_max, "|",cur_min)
        return res_max
        
            
        
                

nums = [2,-5,-2,-4,3]
sol = Solution()
print(sol.maxProduct(nums))
            
            
        
        
