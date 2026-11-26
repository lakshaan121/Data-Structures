class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        dict1={}
        adj=[[] for _ in range(len(edges)+2)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        for i in adj:
            if len(i)>1:
                return adj.index(i)
