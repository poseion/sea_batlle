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

def is_valid_position(board, ship, orientation, row, col):
    if orientation == "H":
        for i in range(ship):
            if col + i >= 7 or board[row][col + i] != " ":
                return False
    else:
        for i in range(ship):
            if row + i >= 7 or board[row + i][col] != " ":
                return False
    return True
    
def place_ship(board, ship, orientation):
    while True:
        row = random.randint(0, 6)
        col = random.randint(0, 6)
        if is_valid_position(board, ship, orientation, row, col):
            if orientation == "H":
                for i in range(ship):
                    board[row][col + i] = str(ship)
            else:
                for i in range(ship):
                    board[row + i][col] = str(ship)
            break
def player_shot(board, shots):
    while True:
        try:
            user_input = input("Enter your shot (e.g., A5): ").upper()
            if len(user_input) == 2 and "A" <= user_input[0] <= "G" and "1" <= user_input[1] <= "7":
                row = int(user_input[1]) - 1
                col = ord(user_input[0]) - ord("A")
                if board[row][col] == " ":
                    board[row][col] = "M"
                    print("Miss!")
                elif board[row][col] == "H":
