class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left=0
        count=0
        dict1={}
        substr=""
        dict2={}
        dup=0
        for right in range(len(s)):
            if s[right] not in dict1:
                dict1[s[right]]=1
            else:
                dict1[s[right]]+=1
            while left<len(s) and (len(dict1)>maxLetters or(right-left+1)>maxSize):
                dict1[s[left]]-=1
                if dict1[s[left]]==0:
                    del dict1[s[left]]
                left+=1
            start=left
            substr=s[left:right+1]
            print(substr)
            if len(substr)>=minSize:
                if substr not in dict2:
                    dict2[substr]=1
                else:
                    dict2[substr]+=1
            substr1=substr
            while len(substr1)>=minSize:
                substr1=s[start+1:right+1]
                if substr1 not in dict2 and len(substr1)>=minSize:
                    dict2[substr1]=1
                    print(substr1)
                elif substr1 in dict2:
                    dict2[substr1]+=1
                    print(substr1)
                start+=1
        if len(dict2)==0:
            return 0
        return max(dict2.values())
