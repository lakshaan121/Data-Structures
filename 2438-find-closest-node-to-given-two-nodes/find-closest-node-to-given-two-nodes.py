class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        adj=[[] for _ in range(len(edges))]
        d1=[-1]*len(edges)
        current_min=float('inf')
        current_node=-1
        d2=[-1]*len(edges)
        self.visited=set()
        for i in range(len(edges)):
            adj[i].append(edges[i])
        def dfs(node,count,distance):
            if node==-1 or node in self.visited:
                return
            self.visited.add(node)
            distance[node]=count
            for neighbour in adj[node]:
                dfs(neighbour,count+1,distance)
        dfs(node1,0,d1)
        self.visited=set()
        dfs(node2,0,d2)
        for i in range(len(d1)):
            if d1[i]==-1 or d2[i]==-1:
                continue
            else:
                if max(d1[i],d2[i])<current_min:
                    current_node=i
                    current_min=max(d1[i],d2[i])
        return current_node
            
