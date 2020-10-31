import gameboard
import player

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
# Create a new Player called player starting at position 3,2

board = gameboard.GameBoard()
player = player.Player(3, 2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
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
        break
