class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        dict1={}
        count=0
        for i in range(len(time)):
            remainder=time[i]%60
            needed=(60-remainder)%60
            if needed in dict1:
                count+=dict1[needed]
            if remainder not in dict1:
                dict1[remainder]=1
            else:
                dict1[remainder]+=1
                
        return count
