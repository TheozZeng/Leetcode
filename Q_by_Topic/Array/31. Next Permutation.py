from bisect import bisect_left 

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1,0,-1):
            if(nums[i-1] < nums[i]):
                n = nums[i-1]
                partial_L = sorted(nums[i-1:])
                #print(nums[:i-1],"|",partial_L)
                
                index = bisect_left(partial_L, n)
                while(partial_L[index] == n):
                    #print(index, partial_L[index])
                    index += 1
                next_smaller = partial_L[index]
                
                partial_L.remove(next_smaller)
                nums[:] = nums[:i-1] + [next_smaller] + partial_L
                return
        nums.sort()
        return

sol = Solution()
nums = [1,3,2]
sol.nextPermutation(nums)
print(nums)
