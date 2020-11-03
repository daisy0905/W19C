import gameboard
import player
import enemies
import random
import coin

print("Welcome to the game!")
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

board = gameboard.GameBoard()
player = player.Player(9, 1)
enemy = enemies.Enemy(5, 5)
# enemy_two = enemies.Enemy(9, 9)
player.rowPosition = 9
player.columnPosition =  1
enemyLastRow = 0
enemyLastCol = 0
score = 0
coins = [coin.Coin(1, 3), coin.Coin(1,4), coin.Coin(3, 3), coin.Coin(3, 4), coin.Coin(5, 6), coin.Coin(5, 7), coin.Coin(5, 8), coin.Coin(1, 7), coin.Coin(1, 8), coin.Coin(5, 2)]


while True:
    if enemy.enemyCheck(player.rowPosition, player.columnPosition, enemyLastRow, enemyLastCol):
        break
    for coin in coins:
        if coin.coinCollect(player.rowPosition, player.columnPosition):
            score += 1
    board.printBoard(player.rowPosition, player.columnPosition, enemy.enemyRow, enemy.enemyColumn, coin.coinRow, coin.coinColumn)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!

    if selection == "w":
        check_move = board.checkMove(player.rowPosition - 1, player.columnPosition)
        if check_move == True:
            player.moveUp()
    elif selection == "s":
        check_move = board.checkMove(player.rowPosition + 1, player.columnPosition)
        if check_move == True:
            player.moveDown()
    elif selection == "a":
        check_move = board.checkMove(player.rowPosition, player.columnPosition - 1)
        if check_move == True:
            player.moveLeft()
    elif selection == "d":
        check_move = board.checkMove(player.rowPosition, player.columnPosition + 1)
        if check_move == True:
            player.moveRight()
        
    check_win = board.checkWin(player.rowPosition, player.columnPosition)
    if check_win == True:
        print("Congratulations, you win!")
        print("Your score is: " + str(score))
        break

    while True:
        enemyMove = random.randint(1, 4)
        enemyLastCol = enemy.enemyColumn
        enemyLastRow = enemy.enemyRow

        if enemyMove == 1:
            enemy_check_move = board.checkMove(enemy.enemyRow - 1, enemy.enemyColumn)
            if enemy_check_move == True:
                enemy.moveUp()
                break
        elif enemyMove == 2:
            enemy_check_move = board.checkMove(enemy.enemyRow + 1, enemy.enemyColumn)
            if enemy_check_move == True:
                enemy.moveDown()
                break
        elif enemyMove == 3:
            enemy_check_move = board.checkMove(enemy.enemyRow, enemy.enemyColumn - 1)
            if enemy_check_move == True:
                enemy.moveLeft()
                break
        elif enemyMove == 4:
            enemy_check_move = board.checkMove(enemy.enemyRow, enemy.enemyColumn + 1)
            if enemy_check_move == True:
                enemy.moveRight()
                break
            

