class Solution:
    def maxArea(self, height):
        max_area = 0
        l = 0
        r = len(height)-1
        left_move = True
        right_move = True
        while(l < r and (left_move or right_move)):
            h_l = height[l]
            h_r = height[r]
            w = r -l
            h = min(h_l,h_r)
            Area = w*h
            max_area = max(max_area,Area)
            print(l,":",r, "|", max_area, end = " ")
            # check need l ++
            if(l+1 <= r and left_move):
                h_l_new  = height[l+1]
                A_less = h_l * 1
                A_more = (h_l_new - h_l)*(r-(l+1))
                if(A_more > A_less):
                    l += 1
                else:
                    left_move = False
                
                
            # check need r --
            elif(l<= r-1 and right_move):
                h_r_new  = height[r-1]
                A_less = h_r * 1
                A_more = (h_r_new - h_r)*(r-1-l)
                if(A_more > A_less):
                    r -= 1
                else:
                    right_move = False
                    
            print(left_move, right_move)
                    
        return max_area
    

sol = Solution()
height = [2,3,4,5,18,17,6]
print(sol.maxArea( height ))
