class Solution:
    def countValidSubstrings(self, s: str) -> int:
        left=0
        last=-1
        count=0
        dict1={'a':0,'b':1,'c':2}
        for right in range(len(s)):
            if right>1:
                if s[right-2:right+1]=='abc':
                    last=right-2
            count+=right-last
        return count