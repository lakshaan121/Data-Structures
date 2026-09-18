class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m=len(board)
        n=len(board[0])
        def f(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if board[i][j]!='O':
                return
            board[i][j]='#'
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
                if board[i][j]=='#':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        return board
        