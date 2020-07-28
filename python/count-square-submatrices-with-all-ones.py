class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        total = 0
        
        for i in range(m):
            dp[i][0] = matrix[i][0]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                total +=dp[i][j]
        
        return total
                
        
