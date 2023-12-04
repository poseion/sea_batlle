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
                    print("You already shot this ship. Try again.")
                else:
                    ship_size = int(board[row][col])
                    board[row][col] = "H"
                    if all("H" in row for row in board):
                        print_board(board, hide_ships=False)
                        print("Congratulations! You sank all the ships!")
                        print(f"Number of shots: {shots}")
                        return True
                    else:
                        print("Hit!")
                        if all(board[i][col] == "H" for i in range(row, row + ship_size)):
                            print(f"You sank a ship of size {ship_size}!")
                        if all(board[row][j] == "H" for j in range(col, col + ship_size)):
                            print(f"You sank a ship of size {ship_size}!")
                return False
            else:
                print("Invalid input. Please enter a valid shot (e.g., A5).")
        except ValueError:
            print("Invalid input. Please enter a valid shot (e.g., A5).")
def play_game():
    player_name = input("Enter your name: ")
    clear_screen()

    # Initialize the board
    board = [[" " for _ in range(7)] for _ in range(7)]

    # Place ships on the board
    place_ship(board, 3, random.choice(["H", "V"]))
    place_ship(board, 2, random.choice(["H", "V"]))
    place_ship(board, 2, random.choice(["H", "V"]))
    place_ship(board, 1, random.choice(["H", "V"]))
    place_ship(board, 1, random.choice(["H", "V"]))
    place_ship(board, 1, random.choice(["H", "V"]))
    place_ship(board, 1, random.choice(["H", "V"]))

    shots = 0
    while True:
        print_board(board)
        if player_shot(board, shots):
            break
        shots += 1

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes", player_name, shots

def main():
    players = []
    while True:
        play_again, player_name, shots = play_game()
        players.append((player_name, shots))
        if not play_again:
            clear_screen()
            print("Game Over!")
            print("Top players:")
            players.sort(key=lambda x: x[1])
            for i, (name, shots) in enumerate(players):
                print(f"{i + 1}. {name} - {shots} shots")
            break
