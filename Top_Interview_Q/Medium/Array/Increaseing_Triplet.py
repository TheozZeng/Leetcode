class Solution:
    def increasingTriplet(self, nums) -> bool:
        Min_1 = float("inf")
        Min_2 = float("inf")
        Min_3 = float("inf")
        for i in nums:
            if(i < Min_1):
                Min_1 = i
            elif(Min_1 < i < Min_2 ):
                Min_2 = i
            elif(Min_2 < i):
                return True
            print(Min_1,"|",Min_2,"|",Min_3)
        return False

nums = [1,8,7,2,-1,-2,9]
sol = Solution()
sol.increasingTriplet(nums)
        
