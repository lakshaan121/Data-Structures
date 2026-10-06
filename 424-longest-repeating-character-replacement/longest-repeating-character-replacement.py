
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1={}
        left=0
        max_len=-1
        for right in range(len(s)):
            if s[right] not in dict1:
                dict1[s[right]]=1
            else:
                dict1[s[right]]+=1
            while (right-left+1)-max(dict1.values())>k:
                dict1[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
