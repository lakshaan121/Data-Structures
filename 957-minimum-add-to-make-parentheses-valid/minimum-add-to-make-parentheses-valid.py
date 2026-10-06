class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')' and stack and stack[-1]=='(':
                stack.pop()
            elif s[i]==')' and not stack:
                count+=1
        return len(stack)+count