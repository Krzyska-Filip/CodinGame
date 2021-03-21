#
# HardCoded - It was pretty simple but I gave up anyway.
#
"""
import sys
import math

board = str()
for i in range(3):
    board += input()
board = list(board)

if  (((board[0] == 'O' and board[1] == 'O') or (board[0] == 'O' and board[2] == 'O') or (board[1] == 'O' and board[2] =='O')) and board[0] != 'X' and board[1] != 'X' and board[2] != 'X'):
    board[0], board[1], board[2] = 'O', 'O', 'O'
elif(((board[3] == 'O' and board[4] == 'O') or (board[3] == 'O' and board[5] == 'O') or (board[4] == 'O' and board[5] =='O')) and board[3] != 'X' and board[4] != 'X' and board[5] != 'X'):
    board[3], board[4], board[5] = 'O', 'O', 'O'
elif(((board[6] == 'O' and board[7] == 'O') or (board[6] == 'O' and board[8] == 'O') or (board[7] == 'O' and board[8] =='O')) and board[6] != 'X' and board[7] != 'X' and board[8] != 'X'):
    board[6], board[7], board[8] = 'O', 'O', 'O'

elif(((board[0] == 'O' and board[3] == 'O') or (board[0] == 'O' and board[6] == 'O') or (board[3] == 'O' and board[6] == 'O')) and board[0] != 'X' and board[3] != 'X' and board[6] != 'X'):
    board[0], board[3], board[6] = 'O', 'O', 'O'
elif(((board[1] == 'O' and board[4] == 'O') or (board[1] == 'O' and board[7] == 'O') or (board[4] == 'O' and board[7] == 'O')) and board[1] != 'X' and board[4] != 'X' and board[7] != 'X'):
    board[1], board[4], board[7] = 'O', 'O', 'O'
elif(((board[2] == 'O' and board[5] == 'O') or (board[2] == 'O' and board[8] == 'O') or (board[5] == 'O' and board[8] == 'O')) and board[2] != 'X' and board[5] != 'X' and board[8] != 'X'):
    board[2], board[5], board[8] = 'O', 'O', 'O'

elif(((board[0] == 'O' and board[4] == 'O') or (board[0] == 'O' and board[8] == 'O') or (board[4] == 'O' and board[8] == 'O')) and board[0] != 'X' and board[4] != 'X' and board[8] != 'X'):
    board[0], board[4], board[8] = 'O', 'O', 'O'
elif(((board[2] == 'O' and board[4] == 'O') or (board[2] == 'O' and board[6] == 'O') or (board[4] == 'O' and board[6] == 'O')) and board[2] != 'X' and board[4] != 'X' and board[6] != 'X'):
    board[2], board[4], board[6] = 'O', 'O', 'O'

else:
    board = "false"

if(board == "false"):
    print(board)
else:
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])
"""
