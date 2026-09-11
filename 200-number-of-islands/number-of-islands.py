class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        m=len(grid)
        n=len(grid[0])
        count=0
        def f(i,j):
            if (i<0 or i>=m) or (j<0 or j>=n):
                return 
            if grid[i][j]!='1' or (i,j) in visited:
                return 
            visited.add((i,j))
            up=f(i,j-1)
            down=f(i,j+1)
            left=f(i-1,j)
            right=f(i+1,j)
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=='1':
                    f(i,j)
                    count+=1
        return count


        