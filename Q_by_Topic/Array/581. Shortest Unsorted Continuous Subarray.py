class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        start = None
        end = None
        
        temp_max = - float("inf")
        for i in range(len(nums)):
            n = nums[i]
            #print(i,":",n,"|",temp_max)
            if(n < temp_max):
                end = i
            temp_max = max(temp_max,n)
                
        temp_min = float("inf")       
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            #print(i,":",n,"|",temp_min)
            if(n > temp_min):
                start = i
            temp_min = min(temp_min,n)   
        
        if(start == None):
            return 0
        print(start, "|", end)
        return end-start+1


nums = [1,3,5,7,9,100,98,2,1000]                
sol = Solution()
print(sol.findUnsortedSubarray(nums))
