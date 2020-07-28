class NumArray:
    sumlist = []
    def __init__(self, nums: List[int]):
        if len(nums)==0:
            return 
        self.sumlist = [0]*len(nums)
        self.sumlist[0] = nums[0]
        for i in range(1,len(nums)):
            self.sumlist[i] = nums[i] +self.sumlist[i-1]
        

    def sumRange(self, i: int, j: int) -> int:
        if i ==0:
            return self.sumlist[j]
        return self.sumlist[j]-self.sumlist[i-1]
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
