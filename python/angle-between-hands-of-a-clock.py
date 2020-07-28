class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min = 6
        one_hour = 30
        
        hour_angle = minutes*0.5 + hour%12*one_hour
        min_angle = minutes*one_min
        angle = abs(hour_angle-min_angle)
        if angle>180:
            angle = 360-angle
        return angle
        
        
        
