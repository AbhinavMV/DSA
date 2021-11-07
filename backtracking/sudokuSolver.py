class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isSafe(row,column,element):
            #check the if row and column value is within range of the list
            if(row<0 or row>=len(board) or column<0 or column>=len(board[0])):
                return False
            #check if the element is already present in the row
            for i in board[row]:
                if(i==element):
                    return False
            #check if the element is already present in the column
            for i in range(len(board)):
                if(board[i][column]==element):
                    return False
            #check if the element is present in a 3x3 box
            startRow = row-(row%3) #find starting row value of current 3x3 box
            startColumn = column-(column%3) #find starting column value of current 3x3 box
            for i in range(startRow,startRow+3):
                for j in range(startColumn,startColumn+3):
                    if(board[i][j]==element):
                        return False
            #if none of the above cases return False then element is valid
            return True
        
        #idea - find an empty element in list and check all the values from(1-9) using backtracking
        #Once all the spaces are filled return True
        def solve(board):
            emptyPresent = False
            row=-1
            col=-1
            #Try to find an empty(value='.') in the board list
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j]=='.'):
                        row=i
                        col=j
                        emptyPresent = True
                        break
                if(emptyPresent):
                    break
            #base condition if no empty value exits. Then sudoku is solved.
            if(emptyPresent==False):
                return True
            #if empty element is found fill values from 1-9
            for i in range(1,10):
                #check if element can be filled in the current row,colum
                if(isSafe(row,col,str(i))):
                    board[row][col] = str(i)
                    ans = solve(board)
                    if(ans):
                        return True 
                    else:
                        # if we get False from recursion we backtrack
                        board[row][col] = '.'
            return False
        return solve(board)