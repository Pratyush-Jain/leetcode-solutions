class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        if len(s) ==0:
            return True
        for i in range(len(t)):
            if t[i] == s[counter]:
                counter+=1
            if counter==len(s):
                return True
        if counter == len(s):
            return True
        else:
            return False
        
