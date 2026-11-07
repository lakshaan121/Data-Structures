class Solution:
    def countValidSubstrings(self, s: str) -> int:
        dict1={'a':0,'b':0}
        right1=-1
        last=-1
        last2=-1
        count=0
        for right in range(len(s)):
            if s[right]=='a':
                right1=right
            if s[right]=='b' and right1!=-1:
                last2=right1
            if s[right]=='c' and last2!=-1:
                last=max(last,last2)
            count+=right-last
        return count
                
        