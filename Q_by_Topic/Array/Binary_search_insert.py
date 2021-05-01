class Solution:
    def searchInsert(self, nums , target: int) -> int:
        i = 0
        j = len(nums)-1
        while(i <= j):
            print(i,"|",j,"|",nums[i:j+1])
            mid = (i+j)//2
            if(target == nums[mid]):
                return mid
            elif(target < nums[mid]):
                j = mid - 1
            elif(target > nums[mid]):
                i = mid +1
                
        return i

nums = [1,3,5,6]
target = 19
sol = Solution()
print(sol.searchInsert(nums,target))
