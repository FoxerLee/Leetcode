class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        width = len(board)
        length = len(board[0])
        
        
        for i in range(width):
            for j in range(length):
                if i == 0 or i == width - 1 or j == 0 or j == length - 1:
                    if board[i][j] == 'O':
                        self.DFS(board, i, j)
                        
                        
        for i in range(len(board)):          
            for j in range(len(board[i])):
                if(board[i][j]=='#'):             
                    board[i][j]='O'
                else:
                    board[i][j]='X' 
                    
    def DFS(self, board, i, j):
        if (i<0 or i>=len(board) or j<0 or j>=len(board[i]) or board[i][j]=='X'):
            return None
        if board[i][j]=='#':             
            return None
        board[i][j]='#'
        self.DFS(board, i-1, j)
        self.DFS(board, i, j-1)
        self.DFS(board, i, j+1)
        self.DFS(board, i+1, j)
        
        
