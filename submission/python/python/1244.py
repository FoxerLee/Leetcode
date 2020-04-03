class Leaderboard:

    def __init__(self):
        self.board = collections.defaultdict(int)
        
        

    def addScore(self, playerId: int, score: int) -> None:
        pre_score = self.board.get(playerId, -1)
        if pre_score == -1:
            self.board[playerId] = score
        else:
            self.board[playerId] += score
            

    def top(self, K: int) -> int:
        return sum(sorted(self.board.values())[-K:])
        

    def reset(self, playerId: int) -> None:
        self.board.pop(playerId)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
