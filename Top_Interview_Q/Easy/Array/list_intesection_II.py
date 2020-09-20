class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        D = {}
        for i in nums1:
            if(i not in D):
                D[i]=1
            else:
                D[i]+=1
                
            
        common = []
        for i in nums2:
            if(i in D):
                D[i]-=1
                if(D[i]>=0):
                    common.append(i)
                
                
        return common

nums1 = [1,2,2,1]
nums2 = [2,2] 
sol = Solution()
print(sol.intersect(nums1, nums2))    