class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        mask=0
        sum1=0
        result=[-1]*len(queries)
        prefix=[-1]*len(arr)
        for i in range(len(arr)):
            mask=mask^arr[i]
            prefix[i]=mask
        for i in range(len(queries)):
            start=queries[i][0]
            end=queries[i][1]
            if start==0:
                result[i]=prefix[end]
            elif start==end:
                result[i]=arr[start]
            else:
                result[i]=prefix[end]^prefix[start-1]
        print(prefix)
        return result
