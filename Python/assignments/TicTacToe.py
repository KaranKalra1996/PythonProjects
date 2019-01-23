class TicTacToe():
    gameBoard = [["1","2","3"],["4","5","6"],["7","8","9"]]
    def __init__(self,player1,player2):
        self.player1 = player1 
        self.player2 = player2
    def findIndex(self, position):
        for indexOfRow,Row in enumerate(self.gameBoard) :
            if position in Row:
                return (indexOfRow, Row.index(position))
        return 3,3

    def PrintBoard(self):
        for i in range(0,3):
            print(self.gameBoard[i])
    def StartGame(self):
        self.PrintBoard()
        flag = 0
        P1 = True
        P2 = True
        for i in range(0,9):
            P1 = True
            P2 = True
            while(P1) : 
                position = input("Player1 Turn, Enter position : ")
                if self.Turn(self.player1,position) : 
                    P1 = False
            self.PrintBoard()
            if self.CheckWinner():
                print(self.player1+" is Winner, Congratulations.")
                flag = 1
                break
            while(P2) :
                position = input("Player2 Turn, Enter position : ")
                if self.Turn(self.player2,position) :
                    P2 = False
            self.PrintBoard()
            if self.CheckWinner():
                print(self.player2+" is Winner, Congratulations.")
                flag = 1
                break
        if flag == 0:
            print("Draw!")

        
    def CheckWinner(self):
        for i in range(0,3):
            if self.gameBoard[i][0] == self.gameBoard[i][1] and self.gameBoard[i][1]==self.gameBoard[i][2] :
                return True
            elif self.gameBoard[0][i] == self.gameBoard[1][i] and self.gameBoard[1][i]==self.gameBoard[2][i]:
                return True
        if self.gameBoard[0][0] == self.gameBoard[1][1] and self.gameBoard[1][1] == self.gameBoard[2][2]:
            return True
        elif self.gameBoard[0][2] == self.gameBoard[1][1] and self.gameBoard[1][1] == self.gameBoard[2][0]:
            return self.gameBoard[0][2]
        return False
    def Turn(self,player,position):
        i,j = self.findIndex(position)
        if i!= 3 :
            if player == self.player1:
                self.gameBoard[i][j] = "X"
            else :
                self.gameBoard[i][j] = "0"
            return True
        else :
            print("This place is already occupied.")
            return False



player1 = input("Player1 name (X) : ")
player2 = input("Player2 name (0) : ")
gameObj = TicTacToe(player1,player2)
gameObj.StartGame()



