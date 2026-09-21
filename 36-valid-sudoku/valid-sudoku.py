class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        visited=set()
        dict1={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
        dict2={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
        dict3={
            (0,0):set(), (0,1):set(), (0,2):set(),
            (1,0):set(), (1,1):set(), (1,2):set(),
            (2,0):set(), (2,1):set(), (2,2):set()
        }
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]=='.':
                    continue
                if board[i][j] in dict1[i] or board[i][j] in dict2[j] or board[i][j] in dict3[(i//3,j//3)]:
                    return False
                dict1[i].add(board[i][j])
                dict2[j].add(board[i][j])
                dict3[(i//3,j//3)].add(board[i][j])

        return True