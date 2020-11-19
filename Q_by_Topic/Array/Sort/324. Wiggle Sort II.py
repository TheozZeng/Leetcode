class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if(len(nums)%2 == 0):
            mid = len(nums)//2 -1
        else:
            mid = len(nums)//2 
        
        L = [None]*len(nums)
        index = 1
        for i in range(len(nums)-1,mid,-1):
            L[index] = nums[i]
            index += 2
        index = 2
        for i in range(mid -1 ,-1,-1):
            L[index] = nums[i]
            index += 2
        L[0] = nums[mid]
        nums[:] = L

# 1 2 3 3 3 4 5
#          |
# 5 * 4 * 3
#*  3 * 2 * 1
#3 5 3 4 2 3 1
