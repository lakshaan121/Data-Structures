class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix=[-1]*len(words)
        sum1=0
        result=[-1]*len(queries)
        visited={'a','e','i','o','u'}
        for i in range(len(words)):
            if words[i][0] in visited and words[i][-1] in visited:
                words[i]=1
            else:
                words[i]=0
            sum1+=words[i]
            prefix[i]=sum1
        for i in range(len(queries)):
            if queries[i][0]==0:
                result[i]=prefix[queries[i][1]]
            else:
                result[i]=prefix[queries[i][1]]-prefix[queries[i][0]-1]
        print(prefix)
        return result
