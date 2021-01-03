class Solution:
    def maxSlidingWindow(self, nums, k) :
        size = len(nums) - k
        L = []
        
        # note temp_max count
        tmp_max_count = (None,None)
        
        for i in range(size+1):
            #print(nums[i:i+k])
            if(i == 0):
                tmp_max = max(nums[i:i+k])
                count = nums[i:i+k].count(tmp_max)
                
                
            else:
                prev_tmp_max = tmp_max_count[0]
                prev_count = tmp_max_count[1]
                num_omit = nums[i-1]
                num_add = nums[i+k-1]
                #print(num_omit,":",num_add)

                #deal with num_omit
                if(num_omit == prev_tmp_max):
                    prev_count -= 1

                # deal with num_add
                if(num_add == prev_tmp_max):
                    tmp_max = prev_tmp_max
                    if(prev_count == 0):
                        count = 1
                    else:
                        count = prev_count + 1
                    
                elif(num_add > prev_tmp_max):
                    tmp_max = num_add
                    count = 1
                    
                else:
                    if(prev_count == 0):
                        tmp_max = max(nums[i:i+k])
                        count = nums[i:i+k].count(tmp_max)
                    else:
                        tmp_max = prev_tmp_max
                        count = prev_count


            L.append(tmp_max)
            tmp_max_count = (tmp_max,count)
            #print(tmp_max_count)
        return L
                    
                
                    
                   
                    
        
                
                

nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol = Solution( )
print(sol.maxSlidingWindow(nums,k))
