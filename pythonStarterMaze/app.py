import gameboard
import player
import enemies
import random

print("Welcome to the game!")
print("Please enter coins number: ")
coinsAmount = int(input())
print("Please enter enemy number: ")
enemiesAmount = int(input())
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called player starting at position 9,1

board = gameboard.GameBoard(coinsAmount)
board.coinsPosition()
player = player.Player(9, 1)
enemy = []
enemyPosition = []
player.rowPosition = 9
player.columnPosition =  1
enemyLastRow = 8
enemyLastCol = 8

for i in range(enemiesAmount):
    while True:
        row = random.randint(1, 9)
        column = random.randint(1, 9)
        if board.board[row][column].find("*") == -1:
            enemy.append(enemies.Enemy(row, column))
            enemyPosition.append({'row': row, 'column': column, 'lastRow': 8, 'lastColumn': 8})
            break


coinScore = 0

while True:
    if_die = False
    board.printBoard(player.rowPosition, player.columnPosition, enemyPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!

    if selection == "w":
        if board.checkMove(player.rowPosition - 1, player.columnPosition):
            player.moveUp()
    elif selection == "s":
        if board.checkMove(player.rowPosition + 1, player.columnPosition):
            player.moveDown()
    elif selection == "a":
        if board.checkMove(player.rowPosition, player.columnPosition - 1):
            player.moveLeft()
    elif selection == "d":
        if board.checkMove(player.rowPosition, player.columnPosition + 1):
            player.moveRight()

    if board.checkWin(player.rowPosition, player.columnPosition):
        print("Congratulations, you win!")
        print("Your coins collected are: " + str(coinScore) + "/" + str(coinsAmount))
        score = coinScore
        print("Your score is: " + str(score))
        break
    
    for e in range(len(enemy)):
        enemy[e].enemyMove()
        enemyPosition[e]['row'] = enemy[e].enemyRow
        enemyPosition[e]['column'] = enemy[e].enemyColumn
        enemyPosition[e]['lastRow'] = enemy[e].lastRow
        enemyPosition[e]['lastColumn'] = enemy[e].lastColumn
        if enemy[e].enemyCheck(player.rowPosition, player.columnPosition):
            if_die = True
    if if_die == True:
        break
   
    if board.coinScore(player.rowPosition, player.columnPosition):
        coinScore += 1


