class Solution:
    def maxArea(self, height):
        max_area = 0
        l = 0
        r = len(height)-1
        
        while(l < r):
            h_l = height[l]
            h_r = height[r]
            w = r -l
            h = min(h_l,h_r)
            Area = w*h
            max_area = max(max_area,Area)
            if(h_l < h_r):
                l += 1
            else:
                r -= 1
                    
        return max_area
    

sol = Solution()
height = [2,3,4,5,18,17,6]
print(sol.maxArea( height ))
