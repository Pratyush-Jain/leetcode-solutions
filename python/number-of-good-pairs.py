class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j:
                    print(i,j)
                    count+=1
        return count
                    
        
