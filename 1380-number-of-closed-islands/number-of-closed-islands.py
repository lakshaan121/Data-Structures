class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        visited=set()
        visited1=set()
        result=[]
        m=len(grid)
        count=0
        n=len(grid[0])
        def f(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]!=0:
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            f(i+1,j)
            f(i-1,j)
            f(i,j+1)
            f(i,j-1)
        def f1(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]!=0:
                return
            if (i,j) in visited1:
                return
            grid[i][j]='#'
            f(i+1,j)
            f(i-1,j)
            f(i,j+1)
            f(i,j-1)
        for i in range(m):
            f(i,0)
            f(i,n-1)
        for j in range(n):
            f(0,j)
            f(m-1,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and ((i,j) not in visited):
                    f1(i,j)
                    count+=1
        return count