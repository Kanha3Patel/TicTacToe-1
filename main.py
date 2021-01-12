board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]


def printBoard(board):
    print()
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

printBoard(['0', '1', '2', '3', '4', '5', '6', '7', '8'])


turn = 'X'
printBoard(board)

for i in range(9): 
  print("It's your turn " + turn + ". Move to which place?")
  move = int(input())
  board[move] = turn
  print("turn: ", turn)
  printBoard(board)
  if(board[0] == board[1] and board[1] == board[2]): 
    if(board[0] != ' '): 
        print("game is over ", turn, " won")
        break
  if turn == 'X':
    turn = 'O'
  elif turn == 'O':
    turn = 'X'


# what code are we going to write to get the value of the very first cell, so at 0 Index
  # HINT: its very similar to line 21


# if X or O makes a line, game
 # X or O won

# if 0, 1, 2 = X
# if 0. 1, 2 = O

# if all of these r equal
  # game over + turn

