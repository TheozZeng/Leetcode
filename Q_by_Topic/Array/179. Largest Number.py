ffrom functools import cmp_to_key

class Solution:
    def is_s1_smaller_s2(self, s1,s2):
        res1 = int(s1 + s2)
        res2 = int(s2 + s1)
        return res1 - res2
                
                    
    def largestNumber(self, nums):
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort( key = cmp_to_key(self.is_s1_smaller_s2), reverse = True)
        res = ""
        all_0 = True
        for s in nums:
            if(s != "0"):
                all_0 = False
            res += s
        if(all_0):
            return "0"
        return res

        
sol = Solution()

nums = ["1","2","4213","421"]
print(sol.largestNumber(nums))
