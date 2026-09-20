class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        index=1
        for i in s:
            j=i.upper()
            pos=ord(j)-ord('A')+1
            rev=27-pos
            sum=sum+rev*index
            index+=1
        return sum
        