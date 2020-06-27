# Linear runtime but not linear memory

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(lambda:0)
        for i in nums:
            d[i]+=1
        for i in d:
            if d[i]==1:
                return i
