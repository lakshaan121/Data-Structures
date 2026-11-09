class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result=[]
        i=0
        intervals.sort()
        while i<len(intervals):
            if not result:
                result.append(intervals[i])
            elif intervals[i][0]<=result[-1][1]:
                result[-1][1]=max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])
            i+=1
        return result