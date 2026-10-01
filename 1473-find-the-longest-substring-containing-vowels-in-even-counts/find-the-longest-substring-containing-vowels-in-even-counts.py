class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dict1={'a':0,'e':1,'i':2,'o':3,'u':4}
        dict2={0:-1}
        mask=0
        max_len=float('-inf')
        for i in range(len(s)):
            if s[i] in dict1:
                mask^=1<<dict1[s[i]]
            if mask in dict2:
                max_len=max(max_len,i-dict2[mask])
            else:
                dict2[mask]=i
        if max_len==float('-inf'):
            return 0
        return max_len
