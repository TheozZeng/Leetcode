class Solution:
    def trap(self, height) -> int:
        bound = []
        for i in range(len(height)):
            bound.append([None,None])
            
        left_max = 0
        for i in range(len(height)):
            bound[i][0] = left_max
            left_max = max(left_max, height[i])
            
        right_max = 0
        for i in range(len(height)-1,-1,-1):
            bound[i][1] = right_max
            right_max = max(right_max, height[i])
            
        tot = 0  
        for i in range(len(height)):
            b = bound[i]
            area = min(b)
            area_for_water = area - height[i]
            tot += max(0, area_for_water)
        return tot
            

        print(bound)






height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))
        
