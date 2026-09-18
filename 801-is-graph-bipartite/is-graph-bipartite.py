class Solution:

    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        visited = set()
        def f(i):
            visited.add(i)
            for neighbour in graph[i]:
                if neighbour not in visited:
                    color[neighbour] = 1 - color[i]
                    if not f(neighbour):
                        return False
                else:
                    if color[neighbour] == color[i]:
                        return False
            return True
        for i in range(n):
            if i not in visited:
                color[i] = 0
                if not f(i):
                    return False
        return True