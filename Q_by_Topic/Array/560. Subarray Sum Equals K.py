class Solution:
    def subarraySum(self, nums, k):
        Dic = {0:1}
        sum_from_start = 0

        # sum[i:j] = sum[:j] - sum[i]
        count = 0
        for i in nums:
            sum_from_start += i
            tar = sum_from_start - k
            if(tar in Dic):
                count += Dic[tar]

            if(sum_from_start in Dic):
                Dic[sum_from_start] += 1
            else:
                Dic[sum_from_start] = 1
            #print(Dic)
        return count

                    
            
        
def print_matrix(L):
    for row in L:
        print(row)



nums = [1,1,1]
k = 2

sol = Solution()
print(sol.subarraySum(nums, k))
