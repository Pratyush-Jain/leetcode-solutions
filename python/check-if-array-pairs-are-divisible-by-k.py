class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        s = sum(arr)
        if s%k ==0:
            return True
        else:
            return False
        
