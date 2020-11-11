import gameboard
import random
board = gameboard.GameBoard(0)


class Enemy: 
    def __init__(self, enemyInitialRow, enemyInitialCol):
        self.enemyRow = enemyInitialRow
        self.enemyColumn = enemyInitialCol
    
    def moveUp(self):
        self.enemyRow -= 1
    
    def moveDown(self):
        self.enemyRow += 1
    
    def moveLeft(self):
        self.enemyColumn -= 1
    
    def moveRight(self):
        self.enemyColumn += 1

    def enemyCheck(self, testRow, testColumn, enemyLastRow, enemyLastCol):
        if testRow == self.enemyRow and testColumn == self.enemyColumn:
            print("You die, game over!")
            return True
        elif testRow == enemyLastRow and testColumn == enemyLastCol:
            print("You die, game over!")
            return True
        else:
            return False

    def enemyMove(self):
        while True:
            enemyMove = random.randint(1, 4)
            self.enemyLastCol = self.enemyColumn
            self.enemyLastRow = self.enemyRow

            if enemyMove == 1:
                if board.checkMove(self.enemyRow - 1, self.enemyColumn):
                    self.enemyRow -= 1
                    break
            elif enemyMove == 2:
                if board.checkMove(self.enemyRow + 1, self.enemyColumn):
                    self.enemyRow += 1
                    break
            elif enemyMove == 3:
                if board.checkMove(self.enemyRow, self.enemyColumn - 1):
                    self.enemyColumn -= 1
                    break
            elif enemyMove == 4:
                if board.checkMove(self.enemyRow, self.enemyColumn + 1):
                    self.enemyColumn += 1
                    break

