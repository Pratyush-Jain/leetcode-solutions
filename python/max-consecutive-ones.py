class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        curr = 0
        for i in nums:
            if i ==0:
                curr = 0
            else:
                curr +=1
            mx = max(mx,curr)
        return mx
