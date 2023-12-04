import os
import random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def print_board(board, hide_ships=True):
    print("  A B C D E F G")
    for i in range(7):
        print(f"{i + 1} ", end="")
        for j in range(7):
            if board[i][j] == "H":
                print("H", end=" ")
            elif board[i][j] == "M":
                print("M", end=" ")
            elif hide_ships and board[i][j] != " ":
                print(" ", end=" ")
            else:
                print(board[i][j], end=" ")
        print()
