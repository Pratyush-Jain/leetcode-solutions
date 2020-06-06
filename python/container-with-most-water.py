class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        maxArea = 0
        while(start< end):
            area = (end- start)*min(height[start],height[end])
            maxArea = max(maxArea,area)
            if height[start]<height[end]:
                start +=1
            else:
                end -=1
        return maxArea
