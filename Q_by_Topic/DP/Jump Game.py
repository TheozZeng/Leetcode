class Solution:
    def canJump(self, nums) -> bool:
        max_step = 0
        index = 0
        while(index <= max_step and index < len(nums)):
            max_step = max(index + nums[index], max_step)
            #print(index ,"|", max_step)
            index += 1
            if(max_step >= len(nums)-1):
                return True
        return False

nums = [3,0,8,2,0,0,1]
sol = Solution()
print(sol.canJump(nums))
