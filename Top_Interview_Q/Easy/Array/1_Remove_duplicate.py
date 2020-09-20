class Solution(object):
    def removeDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        [00011222]
        """
        if(len(nums)==0):
            return 0
        
        new_num = nums[0]
        new_index = 0
        
        for i in nums:
           if(i != new_num):
               new_index += 1
               new_num = i
               nums[new_index]=i
               
        new_index+=1

        '''
        for j in range(0,new_index):
            print(nums[j])
        '''

        return new_index
