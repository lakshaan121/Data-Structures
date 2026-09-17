class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        count=0
        visited=set()
        def f(city):
            visited.add(city)
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and neighbour not in visited:
                    f(neighbour)

        for i in range(n):
            if i not in visited:
                count+=1
                f(i)
        return count

        



        
        