class Solution:
    def arrangeCoins(self, n: int) -> int:
	# Using mathematical approach
	# n*(n+1)/2 <=N
	return int((2*n+0.25)**0.5 -0.5)
        
