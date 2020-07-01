class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = n
        start = 0
        new = []
        for i in range(n):
            new.append(nums[start +i])
            new.append(nums[mid+i])
        return new
            
        
