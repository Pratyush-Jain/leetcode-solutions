class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = k
        
        for i in num:
            while stack and stack[-1]>i and n:
                stack.pop()
                n-=1
            stack.append(i)
        answer = "".join(stack[0:len(num)-k]).lstrip("0")
        if len(answer):
            return answer
        else:
            return "0"
