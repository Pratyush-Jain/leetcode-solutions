class Solution:
    def romanToInt(self, s: str) -> int:
        num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value = 0
        i = 0
        while(i<len(s)):
            if i+1<len(s) and num[s[i]]< num[s[i+1]]:
                value += num[s[i+1]] - num[s[i]]
                i+=1
            else:
                value += num[s[i]]
            i+=1
        return value
