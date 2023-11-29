import random

def print_board(board):
    """Prints the game board."""
    for row in board:
        print(" ".join(row))

def create_board(size):
    """Creates a new game board of the specified size."""
    return [["O"] * size for _ in range(size)]

def place_ship(board):
    """Randomly places a ship on the game board."""
    ship_row = random.randint(0, len(board) - 1)
    ship_col = random.randint(0, len(board[0]) - 1)
    return ship_row, ship_col

def get_user_guess(size, previous_guesses):
    """
    Gets the user's guess for the row and column.
    Returns a tuple containing the user's guess (row, col).
    """

    while True:
        try:
            guess_row = int(input(f"Ahoy! Guess Row (1-{size}): ")) - 1
            guess_col = int(input(f"Guess Col (1-{size}): ")) - 1

            if 0 <= guess_row < size and 0 <= guess_col < size and (guess_row, guess_col) not in previous_guesses:
                return guess_row, guess_col
            else:
                if (guess_row, guess_col) in previous_guesses:
                    print("Avast! Ye already guessed those coordinates. Choose a new spot!")
                else:
                    print(f"Avast! Enter valid coordinates (1-{size}).")
        except ValueError:
            print("Avast! Enter valid coordinates (integer values).")
            
def display_ship(board, ship_row, ship_col):
    """Displays a ship on the game board."""
    board[ship_row][ship_col] = "B"

def display_rules():
    """Displays the pirate game rules."""
    print("Ahoy, ye scurvy dog! Welcome to Pirates of the Python!")
    print("Rules:")
    print("1. Each player has 2 battleships on the map if the grid size is 5 or less.")
    print("2. Each player has 5 battleships on the map if the grid size is 6 or more.")
    print("3. The player wins by sinking all the computer's battleships or using all 10 attempts.")
    print("4. Ye can choose the grid size of the game, with a maximum size of 8x8.")
    print("5. Ye can view the game rules.")
    print("6. Each player takes turns guessing the coordinates to attack.")
    print("7. If a guess hits a battleship, it's marked as '!' on the board.")
    print("8. If a guess misses, it's marked as 'X' on the board.")
    print("Yo-ho-ho! Have fun and good luck, me heartie!")

def get_player_name():
    """Gets the player's pirate name."""
    return input("Arrr! What be yer pirate name, matey? ")
    
def get_grid_size():
    """
    Gets the grid size from the player.
    Returns an integer representing the grid size.
    """
    while True:
        try:
            size = int(input("Avast! Choose the grid size (minimum 3, maximum 8): "))
            if 3 <= size <= 8:
                return size
            else:
                print("Blimey! Grid size must be between 3 and 8.")
        except ValueError:
            print("Landlubber! Enter a valid integer.")
def play_game():
    """Main function to embark on a player adventure."""
    display_rules()

    pirate_name = get_player_name()
    grid_size = get_grid_size()

    print(f"Ahoy, {pirate_name}! Let's set sail on a treacherous sea with a grid size of {grid_size}x{grid_size}.")

    player_board = create_board(grid_size)
    computer_board = create_board(grid_size)

    num_ships = 5 if grid_size >= 6 else 2

    player_ships = [(place_ship(player_board)) for _ in range(num_ships)]
    computer_ships = [(place_ship(computer_board)) for _ in range(num_ships)]

    for ship in player_ships:
        display_ship(player_board, ship[0], ship[1])

    player_won = False
    computer_won = False
    player_attempts = 0
    max_attempts = 10
    previous_player_guesses = set()

    while not player_won and not computer_won and player_attempts < max_attempts:
        print("\nPlayer Board:")
        print_board(player_board)
        print(f"Attempts Left - {max_attempts - player_attempts}")

        player_guess_row, player_guess_col = get_user_guess(grid_size, previous_player_guesses)
        previous_player_guesses.add((player_guess_row, player_guess_col))

        hit_ship = any((player_guess_row, player_guess_col) == (ship[0], ship[1]) for ship in computer_ships)

        if hit_ship:
            print("Arrr, well done! Ye hit the computer's battleship!")
        else:
            print("Arrr, ye missed the mark, ye scurvy dog!")

        player_board[player_guess_row][player_guess_col] = "!" if hit_ship else "X"

        # Check if the player won
        player_won = all(player_board[ship[0]][ship[1]] == "!" for ship in computer_ships)

        if player_won:
            break

        # Computer's turn
        print("\nComputer's Turn:")
        computer_guess_row = random.randint(0, len(player_board) - 1)
        computer_guess_col = random.randint(0, len(player_board[0]) - 1)

        hit_ship = any((computer_guess_row, computer_guess_col) == (ship[0], ship[1]) for ship in player_ships)

        if hit_ship:
            print("Shiver me timbers! The computer hit yer battleship!")
        else:
            print("The computer missed! Aye, safe for now!")

        computer_board[computer_guess_row][computer_guess_col] = "!" if hit_ship else "X"

        # Check if the computer won
        computer_won = all(computer_board[ship[0]][ship[1]] == "!" for ship in player_ships)

        player_attempts += 1

        # Display computer's board
        print("\nComputer Board:")
        print_board(computer_board)

    if player_won:
        print(f"Congratulations, {pirate_name}! Ye sunk all the computer's battleships!")
    elif computer_won:
        print(f"Shiver me timbers! The computer sunk all yer battleships, {pirate_name}!")
    else:
        print(f"Ye've used all yer attempts, {pirate_name}. It be a draw!")

    while True:
        play_again = input("Do ye want to set sail again, me heartie? (yes/no): ").lower()
        if play_again in ("yes", "no"):
            break
        else:
            print("Avast! Please enter 'yes' or 'no'.")

    if play_again == "yes":
        return play_game()
    else:
        print(f"Farewell, {pirate_name}! Until our paths cross again on the high seas. Arrr!")
        return False

# Call the main function directly
play_game()