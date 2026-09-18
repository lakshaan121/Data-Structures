class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m=len(heights)
        n=len(heights[0])
        result=[]
        pacific=set()
        atlantic=set()
        def f(i,j,visited,max1):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if (i,j) in visited:
                return
            if heights[i][j]<max1:
                return
            visited.add((i,j))
            max1=heights[i][j]
            f(i+1,j,visited,max1)
            f(i-1,j,visited,max1)
            f(i,j-1,visited,max1)
            f(i,j+1,visited,max1)
        for i in range(m):
            f(i,0,pacific,float('-inf'))
            f(i,n-1,atlantic,float('-inf'))
        for j in range(n):
            f(0,j,pacific,float('-inf'))
            f(m-1,j,atlantic,float('-inf'))

        for i in range(m):
            for j in range(n):
                if ((i,j) in pacific) and ((i,j) in atlantic):
                    result.append([i,j])
        return result