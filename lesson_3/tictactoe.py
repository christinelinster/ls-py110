import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINS_NEEDED = 2
MIDDLE_SQUARE = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]
def prompt(message):
    print(f'==>{message}')

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def choose_starting_player():
    options = ['player', 'computer', 'choose']
    while True:
        prompt(f'Select who starts the game: {', '.join(options)}')
        starting_player = input()

        if starting_player.lower() == 'player':
            return HUMAN_MARKER
        elif starting_player.lower() == 'computer':
            return COMPUTER_MARKER
        elif starting_player.lower() == 'choose':
            return random.choice([HUMAN_MARKER, COMPUTER_MARKER])
        else:
            prompt('That is not a valid choice.')


def empty_squares(board):
    return [key 
            for key, value in board.items()
            if value == INITIAL_MARKER]

def join_or(empty_squares, delimiter = ', ', word = 'or'):
    if len(empty_squares) > 1:
        return (f"{delimiter.join(empty_squares[:len(empty_squares) - 1])}"
               f" {word} {empty_squares[len(empty_squares) - 1]}")
    else: 
        return empty_squares[0]

def select_risky_square(line, board, marker):
    markers_on_board = [board[square] for square in line]
    if markers_on_board.count(marker) == 2: 
        for square in line: 
            if board[square] == INITIAL_MARKER:
                return square
    return None

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square: {join_or(valid_choices)}")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    square = None

    # offense
    for line in WINNING_LINES:
        square = select_risky_square(line, board, COMPUTER_MARKER)
        if square:
            break

    # defense
    if not square:
        for line in WINNING_LINES:
            square = select_risky_square(line, board, HUMAN_MARKER)
            if square:
                break

    # middle or random
    if not square:
        if board[MIDDLE_SQUARE] == INITIAL_MARKER:
            square = MIDDLE_SQUARE
        else:
            square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        values = [board[square] for square in line]
        
        if values.count(HUMAN_MARKER) == 3:
            return 'Player'
        elif values.count(COMPUTER_MARKER) == 3:
            return 'Computer'
    
    return None
    
def display_score(player_score, computer_score):
    prompt(f'Player Score: {player_score}')
    prompt(f'Computer Score: {computer_score}')

def get_score(player_score, computer_score, winner):
    if winner == 'Player':
        player_score += 1
    elif winner == 'Computer':
        computer_score += 1
    return player_score, computer_score

def play_again():
    prompt("Play again? (y or n)")
    answer = input().lower()

    while answer not in ['yes', 'y', 'n', 'no']:
        prompt("Please enter y or n")
        answer = input().lower()
        
    return answer == 'y' or answer == 'yes'

def play_match():
    player_wins = 0
    computer_wins = 0
    starting_player = choose_starting_player()
    while True:
        winner = play_tic_tac_toe(starting_player, player_wins, computer_wins)
        player_wins, computer_wins = get_score(player_wins, computer_wins, winner)
        starting_player = HUMAN_MARKER if starting_player == COMPUTER_MARKER else COMPUTER_MARKER
        if player_wins >= WINS_NEEDED:
            prompt('You win this round!')
            break
        elif computer_wins >= WINS_NEEDED:
            prompt('Computer wins this round!')
            break
    play_again()

def choose_square(board, current_player):
    player_chooses_square(board) if current_player == HUMAN_MARKER else computer_chooses_square(board)

def alternate_player(current_player):
    return HUMAN_MARKER if current_player == COMPUTER_MARKER else COMPUTER_MARKER


def play_tic_tac_toe(current_player, player_score, computer_score):
    board = initialize_board()

    while True:
        display_board(board)
        display_score(player_score, computer_score)
        choose_square(board, current_player)
        current_player = alternate_player(current_player)
        if someone_won(board) or board_full(board):
            break
    
    display_board(board)

    if someone_won(board):
        prompt(f'{detect_winner(board)} won this game!')
        input("Press Enter to continue...")
    else:
        prompt("It's a tie!")
        input("Press Enter to continue...")
        
    return detect_winner(board)

def main():
    while True:
        play_match()
        if not play_again():
            prompt('Thank you for playing!')
            break

main()