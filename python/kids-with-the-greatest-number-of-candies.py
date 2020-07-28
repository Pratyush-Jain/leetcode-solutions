class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
         
            ma = max(candies)
            return[ (i + extraCandies) >= ma for i in candies ]
