class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=[[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        queue=[source]
        visited=set()
        visited.add(source)
        while len(queue)!=0:
            node=queue.pop(0)
            if node==destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False