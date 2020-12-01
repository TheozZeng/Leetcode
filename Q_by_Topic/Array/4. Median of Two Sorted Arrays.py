class Solution:
    '''
    L1:      x1 x2 x3 | x4 x5 x6
    L2:      y1 y2 |  y3

    if (y2 <= x4  &&  x3 <= y3):
        odd max(x3,y2)
    if(x3 > y3):
        partion [x1, x2,x3]
    if (y2 > x4):
        partion [x4,x5,x6]
    '''
    def findMedianSortedArrays(self, nums1, nums2):
        tot_L = len(nums1) + len(nums2)
        is_odd = False
        if(tot_L % 2 == 0):
            half_L = tot_L //2
        else:
            is_odd = True
            half_L = tot_L //2 + 1

        #swap to make len(nums1) < len(nums2)
        if(len(nums1) > len(nums2)):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
            
        lo = 0
        hi = len(nums1)
        
        while(lo <= hi):
            mid1 = (lo + hi)//2
            mid2 = half_L - mid1
            
            print(mid1,":",nums1[:mid1],"|",nums1[mid1:])
            print(mid2,":",nums2[:mid2],"|",nums2[mid2:])
            print("------------------------------------")
            
            if(mid1 == 0):
                left1 = - float("inf")
            else:
                left1 = nums1[mid1 -1]
            if(mid1 == len(nums1)):
                right1 = float("inf")
            else:
                right1 = nums1[mid1]
                
            if(mid2 ==0):
                left2 = - float("inf")
            else:
                left2 = nums2[mid2 -1]
            if(mid2 == len(nums2)):
                right2 = float("inf")
            else:
                right2 = nums2[mid2]
            
            if(left1 <= right2 and left2 <= right1):
                Finish = True
                print("<",left1,left2,right1,right2,">")
                if(is_odd):
                    return max(left1,left2)
                else:
                    return (max(left1,left2) + min(right1,right2))/2
                
            elif(left1 > right2):
                hi = mid1
                               
            else:
                lo = mid1 + 1

nums1 = [1,2,3,6,7]
nums2 = [4,5,8,9,10]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
