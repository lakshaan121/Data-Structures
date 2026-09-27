class Solution:
    def reverseParentheses(self, s: str) -> str:
        start=[]
        pairs=[]
        result=''
        for i in range(len(s)):
            if s[i]=='(':
                start.append(i)
            elif s[i]==')':
                j=start.pop()
                pairs.append((j,i))
        for left,right in pairs:
            s=s[:left] + s[left:right+1][::-1] + s[right+1:]
        for i in s:
            if i.isalnum():
                result+=i
        return result