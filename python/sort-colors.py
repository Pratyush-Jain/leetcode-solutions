class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color = {0:0, 1:0, 2:0}
        sortColor = []
        for i in nums:
            color[i] +=1
        
        for i in color:
            for j in range(color[i]):
                sortColor.append(i)
        for i in range(len(nums)):
            nums[i] = sortColor[i]
