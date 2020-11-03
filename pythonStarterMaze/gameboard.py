import coin

class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 9
        self.board = [
            ["* ", "* ", "* ", "* ", "* ", "* ", "* ", "* ", "* ", "  ", "* "],
            ["* ", "  ", "  ", "  ", "  ", "* ", "  ", "  ", "  ", "  ", "* "],
            ["* ", "  ", "* ", "* ", "  ", "* ", "  ", "* ", "* ", "  ", "* "],
            ["* ", "  ", "* ", "  ", "  ", "  ", "  ", "  ", "* ", "* ", "* "],
            ["* ", "  ", "* ", "* ", "* ", "* ", "  ", "  ", "  ", "  ", "* "],
            ["* ", "  ", "  ", "  ", "  ", "* ", "  ", "* ", "* ", "  ", "* "],
            ["* ", "* ", "  ", "* ", "  ", "* ", "  ", "* ", "* ", "  ", "* "],
            ["* ", "  ", "  ", "* ", "  ", "  ", "  ", "* ", "  ", "  ", "* "],
            ["* ", "  ", "* ", "* ", "  ", "* ", "  ", "* ", "* ", "  ", "* "],
            ["* ", "  ", "  ", "  ", "  ", "* ", "  ", "  ", "  ", "  ", "* "],
            ["* ", "* ", "* ", "* ", "* ", "* ", "* ", "* ", "* ", "* ", "* "]
        ]
        # self.board = [
        #     ["* ", "* ", "  ", "* ", "*"],
        #     ["*  ", " ", " ", " ", "*", " *",],
        #     ["*  ", " ", "* ", "*", " ", "*",],
        #     ["*  ", " ", " ", " ", " ", "*",],
        #     ["* ", "* ", "* ", "* ", "*"],
        # ]
    
    

    def printBoard(self, playerRow, playerColumn, enemyRow, enemyColumn, coinRow, coinColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == enemyRow and j == enemyColumn:
                    print("E ", end="")
                elif i == playerRow and j == playerColumn:
                    print("P ", end="")
                elif i == coinRow and j == coinColumn:
                    print("o ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

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
            print(score)
        return False
    
