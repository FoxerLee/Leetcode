class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [[0 for _ in range(n)] for _ in range(2)]
        self.cols = [[0 for _ in range(n)] for _ in range(2)]
        self.diag = [[0 for _ in range(2)] for _ in range(2)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.rows[player-1][row] += 1
        self.cols[player-1][col] += 1
        if row == col:
            self.diag[player-1][0] += 1
        if (row + col + 1) == self.n:
            self.diag[player-1][1] += 1
            
        if self.rows[player-1][row] == self.n or self.cols[player-1][col] == self.n or self.diag[player-1][0] == self.n or self.diag[player-1][1] == self.n:
            return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
