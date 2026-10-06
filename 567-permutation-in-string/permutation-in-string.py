from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1=dict(Counter(s1))
        dict2={}
        k=len(s1)
        right=0
        left=0
        while right<len(s2):
            if s2[right] not in dict2:
                dict2[s2[right]]=1
            else:
                dict2[s2[right]]+=1
            while (right-left+1)>k:
                dict2[s2[left]]-=1
                if dict2[s2[left]]==0:
                    del dict2[s2[left]]
                left+=1
            if dict1==dict2:
                return True
            right+=1
        return False