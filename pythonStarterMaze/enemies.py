import random

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

import random
print(random.randint(1, 4))