class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        counter = 0
        count = True
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    count = False
            if count:
                counter +=1
            count = True
        return counter
                    
        
