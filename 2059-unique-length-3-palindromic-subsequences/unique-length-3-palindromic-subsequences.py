class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mask=0
        count=0
        dict1={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=[s.find(s[i]),s.rfind(s[i])]
        for ch in dict1:
            mask=0
            if dict1[ch][0]==dict1[ch][1]:
                continue
            else:
                for i in range(dict1[ch][0]+1,dict1[ch][1]):
                    pos=ord(s[i])-ord('a')
                    if mask &(1<<pos):
                        continue
                    else:
                        count+=1
                        mask = mask | (1 << pos)
        print(dict1)
        return count
