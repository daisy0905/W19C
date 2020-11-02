class CoinBoard:
    def __init__(self):
        self.coinBoard = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "o ", "o ", "o ", "o ", "  ", "o ", "o ", "o ", "o ", "  "],
            ["  ", "o ", "  ", "  ", "o ", "  ", "o ", "  ", "  ", "o ", "  "],
            ["  ", "o ", "  ", "o ", "o ", "o ", "o ", "o ", "  ", "  ", "  "],
            ["  ", "o ", "  ", "  ", "  ", "  ", "o ", "o ", "o ", "o ", "  "],
            ["  ", "o ", "o ", "o ", "o ", "  ", "o ", "  ", "  ", "o ", "  "],
            ["  ", "  ", "o ", "  ", "o ", "  ", "o ", "  ", "  ", "o ", "  "],
            ["  ", "o ", "o ", "  ", "o ", "o ", "o ", "  ", "o ", "o ", "  "],
            ["  ", "o ", "  ", "  ", "o ", "  ", "o ", "  ", "  ", "o ", "  "],
            ["  ", "o ", "o ", "o ", "o ", "  ", "o ", "o ", "o ", "o ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        ] 
    
    def printCoinBoard(self, playerRow, playerColumn):
        for i in range(len(self.coinBoard)):
            for j in range(len(self.coinBoard[i])):
                if i == playerRow and j == playerColumn:
                    print("P", end="")
                    score += 1
                    print("Your score: " + str(score))
                else:
                    print(self.coinBoard[i][j], end="")
            print("")