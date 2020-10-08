class Solution:
    def productExceptSelf(self, nums):
        res = []
        
        num_of_0 = 0
        product = 1
        for i in range(len(nums)):
            if(nums[i] == 0):
                num_of_0 += 1
            else:
                product *= nums[i]

        for i in range(len(nums)):
            if(nums[i] == 0):
                if(num_of_0 > 1):
                    res.append(0)
                else:
                    res.append(product)
            elif(num_of_0 >0):
                res.append(0)
            else:
                res.append(product//nums[i])
        return res


nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))


                    
        
        
