import random

class Coin:
    def __init__(self, coinInitialRow, coinInitialCol):
        self.coinRow = coinInitialRow
        self.coinColumn = coinInitialCol
    
    def coinCollect(self, testRow, testColumn):
        if testRow == self.coinRow and testColumn == self.coinColumn:
            return True
        else:
            return False
