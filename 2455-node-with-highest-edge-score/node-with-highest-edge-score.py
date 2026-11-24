class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        dict1={}
        max_node=-1
        max_val=-1
        for i in range(len(edges)):
            if edges[i] not in dict1:
                dict1[edges[i]]=i
            else:
                dict1[edges[i]]+=i
        for key,val in dict1.items():
            if val>max_val:
                max_val=val
                max_node=key
            elif val==max_val:
                if key<max_node:
                    max_node=key
        return max_node