class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #First element is 1 always
        prev = 1
        ans = []
        ans.append(1)
        for i in range(1,rowIndex+1):
            #To write nCr in terms of previous term
            #nCr = (nCr-1+(n-r+1))/r
            curr = prev*(rowIndex-i+1)//i
            ans.append(curr)
            prev = curr
        return ans
