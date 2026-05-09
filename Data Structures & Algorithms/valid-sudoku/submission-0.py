class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for num in row:
                if num == ".":
                    continue
                if num in rowSet:
                    return False
                rowSet.add(num)
        
        for i in range(9):
            colSet = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])
        
        for x in range(3):
            for y in range(3):
                boxSet = set()
                startX = x *3
                startY = y*3
                for i in range(3):
                    for j in range(3):
                        if board[startX +i][startY +j] == ".":
                            continue
                        if board[startX +i][startY +j] in boxSet:
                            return False
                        boxSet.add(board[startX +i][startY +j])
        
        return True

            
        