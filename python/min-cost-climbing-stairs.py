class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==0:
            return 0
        if len(cost)<=2:
            return min(cost)
        c1 = cost[0]
        c2 = cost[1]
        for i in range(2,len(cost)):
            temp = cost[i] + min(c1,c2)
            c1 = c2
            c2 = temp
        return min(c1,c2)
        
