from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        times = 0
        fresh = 0
        rotten = deque()
        row = len(grid)
        cols = len(grid[0])
        
        
        # create queue
        for r in range(row):
            for c in range(cols):
                if grid[r][c] ==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh +=1
        
        while rotten and fresh>0:
            times+=1
            
            for item in range(len(rotten)):
                x,y = rotten.popleft()
                
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    xx,yy = x+dx,y+dy
                    if xx<0 or xx==row or yy<0 or yy==cols:
                        continue
                    if grid[xx][yy] ==2 or grid[xx][yy] ==0:
                        continue
                    fresh-= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        return times if fresh == 0 else -1

        
            
