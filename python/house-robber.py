class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0]*len(nums)
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        rob[0] = nums[0]
        rob[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            rob[i] = max(rob[i-1],nums[i]+rob[i-2])
        return rob[-1]
