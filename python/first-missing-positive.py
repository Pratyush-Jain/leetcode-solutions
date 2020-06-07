class Solution(object):
    def firstMissingPositive(self,nums):
    
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        maxx = max(nums)
        smallest =1
        while smallest in set(nums) and smallest<maxx+1 :
            smallest+=1
        
        return smallest
