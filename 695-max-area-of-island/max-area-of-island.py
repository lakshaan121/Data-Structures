class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        self.count=0
        visited=set()
        visited2=set()
        ans=float('-inf')
        def f(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]==0 or (i,j) in visited:
                return
            self.count+=1
            visited.add((i,j))
            up=f(i+1,j)
            down=f(i-1,j)
            left=f(i,j-1)
            right=f(i,j+1)
        for i in range(m):
            
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited2:
                    self.count=0
                    f(i,j)
                    print(self.count)
                    ans=max(ans,self.count)
                    visited.add((i,j))
        if ans>0:
            return ans
        else:
            return 0