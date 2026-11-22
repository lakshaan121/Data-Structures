class Solution:
    def checkString(self, s: str) -> bool:
        flag=False
        for i in range(len(s)):
            if s[i]=='b':
                flag=True
            if flag and s[i]=='a':
                return False
        return True