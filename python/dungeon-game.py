# Using bottom up dp approach to calculate minimum cost path

class Solution:
    def calculateMinimumHP(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)]for j in range(m) ]
        dp[-1][-1] = abs(grid[-1][-1])+1 if grid[-1][-1]<0 else 1

        # For last column
        for i in range(m-2,-1,-1):
            dp[i][-1] = max(dp[i+1][-1] - grid[i][n-1],1)

        # for last row
        for i in range(n-2,-1,-1):
            dp[-1][i] = max(dp[-1][i+1]-grid[-1][i],1)

        # for rest of the dp
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-grid[i][j],1)
        

        return dp[0][0]

