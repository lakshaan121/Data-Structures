class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        k1=0
        left=0
        for i in num:
            while stack and stack[-1]>i and k1<k:
                k1+=1
                stack.pop()
            stack.append(i)
        while k1<k:
            stack.pop()
            k1+=1
        for i in range(len(stack)):
            if stack[i]!='0':
                break
            left+=1
        if left==len(stack):
            return "0"
        return "".join(stack[left:])