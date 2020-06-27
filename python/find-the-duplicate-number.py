class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using Floyds's tortoise hare algorithm
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        # findingthe start of the loop
        slow = nums[0]
        while slow!= fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast
    
            
        
