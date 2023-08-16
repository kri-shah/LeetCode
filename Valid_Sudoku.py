#probably could be refactored, but runtime beats Beats 87.79%of users with Python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp = set()
        for x in board:
            for z in x:
                if z != '.':
                    if z in temp:
                        return False
                    else:
                        temp.add(z)
            temp = set()
        
        temp2 = set()
        for x in range(9):
            for y in range(9):
                if board[y][x] != '.':
                    if board[y][x] in temp2:
                        return False
                    else:
                        temp2.add(board[y][x])
            temp2 = set()
        
        temp2 = set()

        for z in range(0, 7, 3):
            for w in range(0, 7, 3):
                temp2 = set()
                for x in range(z, z + 3):
                    for y in range(w, w + 3):
                        if board[x][y] != '.':
                            if board[x][y] in temp2:
                                return False
                            else:
                                temp2.add(board[x][y])
        

                
        
        return True
