class Game:
    #board state = represented by bytes with 0 = empty, 1 = X, 2 = O
    def __init__(self):
        self.board = [0, 0, 0, 
                       0, 0, 0, 
                       0, 0, 0]
        self.turn = 1

    def placeMark(self, player, spot):
        if(self.canPlay(player)):
            if(self.board[spot] != 0):
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
        def checkRow(offset, player):
            valid = 0
            for i in range(3):
                if (self.board[i+offset] == player):
                    valid += 1
            return valid == 3
        def checkColumn(player):
            valid = False
            for i in range(3):
                if self.board[0+i] == player and self.board[3+i] == player and self.board[7+i] == player:
                    valid = True
            return valid;
        def checkDiagonal(player):
            valid1 = self.board[0] == player and self.board[4] == player and self.board[8];
            valid2 = self.board[2] == player and self.board[4] == player and self.board[6]
            return valid1 or valid2;
        def checkPlayer(player):
            valid1 =  checkRow(0, player) or checkRow(3, player) or checkRow(6, player)
            valid2 = checkColumn(player)
            valid3 = checkDiagonal(player)
            return valid1 or valid2 or valid3
        myPlayer = 0
        if(checkPlayer(1)):
            myPlayer = 1
        elif(checkPlayer(2)):
            myPlayer = 2
        return myPlayer

    def canPlay(self, player):
        return player == self.turn;