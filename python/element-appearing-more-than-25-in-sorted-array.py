class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common()[0][0]
        
