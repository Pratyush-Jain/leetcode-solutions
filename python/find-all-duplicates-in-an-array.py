class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            if nums[abs(i)-1]<0:
                output.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return output
