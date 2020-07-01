# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low =1
        high= n
        while low<=high:
            mid1 = low +(high-low)//3
            mid2 = high - (high-low)//3
            g1 = guess(mid1)
            g2 = guess(mid2)
            if g1 ==0:
                return mid1
            if g2 ==0:
                return mid2
            elif g1 <0:
                high = mid1-1
            elif g2 >0:
                low = mid2 +1
            else:
                low = mid1+1
                high = mid2-1
