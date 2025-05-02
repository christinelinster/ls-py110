import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINS_NEEDED = 3
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]


def prompt(message):
    print(f'==>{message}')

def display_board(board):
    # os.system('clear')

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

def computer_defense(line, board):
    markers_on_board = [board[square] for square in line]
    if markers_on_board.count(HUMAN_MARKER) == 2: 
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square {join_or(valid_choices)}")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = None
    for line in WINNING_LINES:
        square = computer_defense(line, board)
        if square:
            break

    if not square:
        square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
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

def play_match():
    while True:
        player_wins = 0
        computer_wins = 0

        while True:
            winner = play_tic_tac_toe(player_wins, computer_wins)
            player_wins, computer_wins = get_score(player_wins, computer_wins, winner)

            if player_wins >= WINS_NEEDED:
                prompt('You win this round!')
                break
            elif computer_wins >= WINS_NEEDED:
                prompt('Computer wins this round!')
                break
        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break
    prompt('Thanks for playing!')

def play_tic_tac_toe(player_score, computer_score):
    board = initialize_board()
    while True:
        display_board(board)
        display_score(player_score, computer_score)
        player_chooses_square(board)
        if someone_won(board) or board_full(board):
            break

        computer_chooses_square(board)
        if someone_won(board) or board_full(board):
            break


    if someone_won(board):
        display_board(board)
        prompt(f"{detect_winner(board)} won!")
    else:
        prompt("It's a tie!")
        
    return detect_winner(board)

play_match()