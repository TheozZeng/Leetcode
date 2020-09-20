class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D ={}
        #D store most recent index of a num
        for  i,num in nums:
            if(num in D and i-D[num] <= k):
                return True
            D[num]=i
        return False
