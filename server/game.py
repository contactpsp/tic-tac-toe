class Game:
    #board state = represented by bytes with 0 = empty, 1 = X, 2 = O
    def __init__(self):
        self.board = [0, 0, 0, 
                       0, 0, 0, 
                       0, 0, 0]
        self.turn = 1

    def placeMark(self, player, spot):
        if(self.canPlay(player)):
            if(self.board[spot] != 0 or len(self.board) < spot):
                return False;
            self.board[spot] = player
            if self.turn == 1:
                self.turn = 2;
            else:
                self.turn = 1;
            return True;
    def validateBoard(self, player):
        if(self.checkForWin()  == player):
            print("player ", player, " won")
            return "Win"
        else:
            x = 0
            for i in range(9):
                if(self.board[i] != 0): x += 1
            if(x >= 9): return "Draw"
        return ""
    
    
    def checkForWin(self):    
        winCombos= [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        def checkWin(self, currentPlayer):
            for x in winCombos:
                if (self.board[x[0]] == currentPlayer and self.board[x[1]] == currentPlayer and self.board[x[2]] == currentPlayer):
                    return True
            return False
        myPlayer = 0
        if(checkWin(self, 1)):
            myPlayer = 1
        elif(checkWin(self, 2)):
            myPlayer = 2
        return myPlayer

    def canPlay(self, player):
        return player == self.turn;