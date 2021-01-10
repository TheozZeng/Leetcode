class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_percentage = (minutes%60)/60.0
        min_angle = min_percentage*360
        print(min_percentage, "_", min_angle, "deg")
        
        hour_percentage = (hour%12)/12.0 + min_percentage * (1/12)
        hour_angle =  hour_percentage * 360
        print(hour_percentage, "_", hour_angle, "deg")
        
        angle_difference = abs(hour_angle - min_angle)
        if(angle_difference > 180):
            return 360 - angle_difference
        return angle_difference

hour = 1
minutes = 57
sol = Solution()
print(sol.angleClock(hour, minutes))
