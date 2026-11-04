class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        result=[]
        matrix= [[False] * numCourses for _ in range(numCourses)]
        
        adj=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj[a].append(b)
        def dfs(node,find):
            self.visited.add(node)
            if node==find:
                return True
            
            for neighbour in adj[node]:
                if neighbour not in self.visited: 
                    if dfs(neighbour,find):
                        return True
            return False
        for a,b in queries:
            self.visited=set()
            if dfs(a,b):
                result.append(True)
            else:
                result.append(False)
        return result
        