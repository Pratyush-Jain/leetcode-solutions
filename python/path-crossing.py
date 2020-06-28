class Solution:
    def isPathCrossing(self, path: str) -> bool:
        patha = {(0,0)}
        x,y = 0,0
        for i in path:
            if i =='N': y+=1
            elif i =='S': y-=1
            elif i =='W': x-=1
            else: x+=1
            if (x,y) in patha: return True
            patha.add((x,y))
        return False
        
