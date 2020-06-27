class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
            
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
                
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        return dp[len(A)][len(B)]
