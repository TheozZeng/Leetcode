class Solution:
    def BinarySearch(self,nums,target):
        l=0
        r=len(nums)-1
        while(l <= r):
            print(l,nums[l],"|",r,nums[r])
            mid = (l+r)//2
            if(nums[mid] == target):
                return mid
            elif(target < nums[mid]):
                r = mid-1
            else:
                l = mid+1
        return None
    
    def searchRange(self, nums, target):
        pos = self.BinarySearch(nums,target)
        if(pos == None):
            return [-1,-1]
        l=pos
        r=pos
        while(l>=0):
            if(nums[l]==target):
                l-=1
            else:
                break
        while(r<=len(nums)-1):
            if(nums[r]==target):
                r+=1
            else:
                break
        return[l+1,r-1]
            
nums = [1]
sol =  Solution()
print(sol.BinarySearch(nums,1))
