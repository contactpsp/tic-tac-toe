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
                return;
            self.board[spot] = player
            if self.turn == 1:
                self.turn = 2;
            else:
                self.turn = 1;
    def validateBoard(self, player):
        if(self.checkForWin()  == player):
            print("player ", player, " won")
            return True
        return False
    
    def checkForWin(self):    
        def checkRow(offset, player):
            valid = 0
            for i in range(3):
                if (self.board[i+offset] == player):
                    valid += 1
            return valid == 3
        def checkColumn(offset, player):
            valid = 0
            for i in range(3):
                if(self.board[offset+(i*3)]):
                    valid += 1
            return valid == 3
        def checkDiagonal(player):
            valid1 = self.board[0] == player and self.board[4] == player and self.board[8];
            valid2 = self.board[2] == player and self.board[4] == player and self.board[6]
            return valid1 or valid2;
        def checkPlayer(player):
            valid1 =  checkRow(0, player) or checkRow(3, player) or checkRow(6, player)
            valid2 = checkColumn(0, player) or checkColumn(1, player) or checkColumn(2, player);
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