class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows,columns,wordLen = len(board),len(board[0]),len(word)-1
        
        def solve(r,c,k):
            if(r<0 or r>=rows or c<0 or c>=columns):
                return False
            
            if(board[r][c]=='#'):
                return False
            
            if(board[r][c]!=word[k]):
                return False
            
            if(k==wordLen):
                return True
            
            temp = board[r][c]
            board[r][c] = '#'
            for i,j in ((-1,0),(0,-1),(1,0),(0,1)):
                if(solve(r+i,c+j,k+1)):
                    return True
            board[r][c] = temp
            return False
        
        for i in range(rows):
            for j in range(columns):
                if(solve(i,j,0)):
                    return True
        return False
        
        