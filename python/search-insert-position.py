class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>target:
            return 0
        for i in range(len(nums)):
            if(nums[i]==target or nums[i]>target):
                return i
        return i+1
