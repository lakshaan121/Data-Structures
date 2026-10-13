class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        left=0
        right=0
        chars=set()
        while right<len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
            
        return maxlen




        l
            
        