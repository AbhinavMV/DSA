class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."]*n for _ in range(n)]
        
        def isSafe(board,row,col):
            for i in range(row):
                if(board[i][col]=='Q'):
                    return False
            #Left Diagonal
            i = row-1
            j = col-1
            while(i>=0 and j>=0):
                if(board[i][j]=='Q'):
                    return False
                i-=1
                j-=1
                
            #Right Diagonal
            i = row-1
            j = col+1
            while(i>=0 and j<len(board)):
                if(board[i][j]=='Q'):
                    return False
                i-=1
                j+=1
            return True
        
        def solve(board,row):
            if(row==len(board)):
                temp = []
                for i in board:
                    temp.append(''.join(i))
                results.append(temp)
                return
            for i in range(len(board)):
                if(isSafe(board,row,i)):
                    board[row][i] = 'Q'
                    solve(board,row+1)
                    board[row][i] = '.'
        
        results = []
        solve(board,0)
        return results