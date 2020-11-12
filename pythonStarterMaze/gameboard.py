import random

class GameBoard:
    def __init__(self, coinsAmount):
        self.winningRow = 0
        self.winningColumn = 9
        self.coinsAmount = coinsAmount
        self.coins = []
        self.board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", " ", "*"],
            ["*", " ", " ", " ", " ", "*", " ", " ", " ", " ", "*"],
            ["*", " ", "*", "*", " ", "*", " ", "*", "*", " ", "*"],
            ["*", " ", "*", " ", " ", " ", " ", " ", "*", "*", "*"],
            ["*", " ", "*", "*", "*", "*", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", "*", " ", "*", "*", " ", "*"],
            ["*", "*", " ", "*", " ", "*", " ", "*", "*", " ", "*"],
            ["*", " ", " ", "*", " ", " ", " ", "*", " ", " ", "*"],
            ["*", " ", "*", "*", " ", "*", " ", "*", "*", " ", "*"],
            ["*", " ", " ", " ", " ", "*", " ", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]
        # self.board = [
        #     ["* ", "* ", "  ", "* ", "*"],
        #     ["*  ", " ", " ", " ", "*", " *",],
        #     ["*  ", " ", "* ", "*", " ", "*",],
        #     ["*  ", " ", " ", " ", " ", "*",],
        #     ["* ", "* ", "* ", "* ", "*"],
        # ]
    
    

    def printBoard(self, playerRow, playerColumn, enemyPosition):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                for k in range(len(self.coins)):
                    if i == self.coins[k].get('row') and j == self.coins[k].get('column'):
                        self.board[i][j] = "O"
                for e in range(len(enemyPosition)):
                    if i == enemyPosition[e].get('row') and j == enemyPosition[e].get('column'):
                        self.board[i][j] = "E"
                    elif i == enemyPosition[e].get('lastRow') and j == enemyPosition[e].get('lastColumn'):
                        self.board[i][j] = " "
                if i == playerRow and j == playerColumn:
                    print("P", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print("")

    def coinsPosition(self):
        for i in range(self.coinsAmount):
            while True:
                row = random.randint(1, 9)
                column = random.randint(1, 9)
                if self.board[row][column].find("*") == -1:
                    if len(self.coins) == 0:
                        coinLocation = {'row': row, 'column': column}
                        self.coins.append(coinLocation)
                    else:
                        if_add = True
                        for coin in self.coins:
                            if row == coin.get('row') and column == coin.get('column'):
                                if_add = False
                        if if_add:
                            coinLocation = {'row': row, 'column': column}
                            self.coins.append(coinLocation)
                    break

    def coinScore(self, coinRow, coinColumn):
        for r in range(len(self.coins)):
            if coinRow == self.coins[r].get('row') and coinColumn == self.coins[r].get('column'):
                print("Score + 1")
                self.coins.remove({'row': coinRow, 'column': coinColumn})
                self.board[coinRow][coinColumn] = " "
                return True

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if playerRow == self.winningRow and playerColumn == self.winningColumn:
            return True
        return False
    
