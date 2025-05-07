import random
import os

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['H', 'D', 'S', 'C']
DECK = [[suit, value] for suit in SUITS for value in VALUES]
BUST_VALUE = 21
DEALER_HIT_VALUE = 17
WINS_NEEDED = 2

def prompt(message):
    print(f'==> {message}')


def initialize_deck():
    deck = [f'{value}{suit}' for suit in SUITS for value in VALUES]
    random.shuffle(deck)
    return deck


def total(cards):
    values = [card[:-1] for card in cards]

    total_sum = 0
    for value in values:
        if value == 'A':
            total_sum += 11
        elif value in ('J', 'Q', 'K'):
            total_sum += 10
        else:
            total_sum += int(value)

    aces = values.count('A')
    while total_sum > 21 and aces:
        total_sum -= 10
        aces -= 1

    return total_sum


def busted(total_value):
    return total_value > BUST_VALUE


def display_hand(cards):
    return ', '.join(cards)


def player_turn(deck, player_cards, player_total):
    while True:
        answer = input('hit or stay? (h / s): ').lower()
        valid_choices = ('h', 's')

        if answer and answer[0] not in valid_choices:
            prompt('Please enter a valid input')
            continue

        os.system('clear')
        if answer.startswith('s'):
            break
        if answer.startswith('h'):
            deal(deck, player_cards)
            player_total = total(player_cards)
            prompt(f'Your cards are: {display_hand(player_cards)}')
            prompt(f'Your total value is {player_total}')

        if busted(player_total):
            break
    return player_total


def dealer_turn(deck, dealer_cards, dealer_total):
    while True:
        if dealer_total >= DEALER_HIT_VALUE or busted(dealer_total):
            break
        deal(deck, dealer_cards)
        dealer_total = total(dealer_cards)
    return dealer_total


def deal(deck, cards):
    cards.append(deck.pop())


def deal_starting_cards(deck, player_cards, dealer_cards):
    for _ in range(2):
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())


def calculate_results(player_total, dealer_total):
    os.system('clear')
    if player_total > BUST_VALUE:
        prompt('Busted! Dealer wins')
        return 'Dealer'
    elif dealer_total > BUST_VALUE:
        prompt('Dealer busted. You win!')
        return 'Player'
    elif player_total > dealer_total:
        prompt('You win!')
        return 'Player'
    elif player_total < dealer_total:
        prompt('Dealer wins!')
        return 'Dealer'
    
    prompt('Tie game!')
    return None


def display_results(player_cards, dealer_cards, player_total, dealer_total):

    prompt(f'Your cards were: {display_hand(player_cards)} '
           f'with a total value of {player_total}')
    prompt(f'The dealer\'s cards were: {display_hand(dealer_cards)} '
           f'with a total value of {dealer_total}')


def play_twenty_one(wins):
    os.system('clear')
    display_score(wins)
    current_deck = initialize_deck()
    player_cards = []
    dealer_cards = []

    deal_starting_cards(current_deck, player_cards, dealer_cards)
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)

    prompt(f'The dealer\'s cards are: ?, {dealer_cards[1]}')
    prompt(f'Your cards are: {display_hand(player_cards)} with a total value of {player_total}')
    
    player_total = player_turn(current_deck, player_cards, player_total)

    if not busted(player_total):
        dealer_total = dealer_turn(current_deck, dealer_cards, dealer_total)
    
    winner = calculate_results(player_total, dealer_total)
    display_results(player_cards, dealer_cards, player_total, dealer_total)
    return winner 


def get_score(winner, wins):
    if winner == 'Player':
        wins['Player'] += 1
    elif winner == 'Dealer':
        wins['Dealer'] += 1

    return wins

def display_score(wins):
    prompt(f'Player Score: {wins['Player']}')
    prompt(f'Dealer Score: {wins['Dealer']}')

def play_match():
    wins = {'Player': 0, 'Dealer': 0}
    while True:
        winner = play_twenty_one(wins)
        if not winner:
            input('Press Enter to play the next game.')
            continue
        wins = get_score(winner, wins)
        
        if wins['Player'] >= WINS_NEEDED:
            prompt('You win this round!')
            break 
        if wins['Dealer'] >= WINS_NEEDED:
            prompt('You lost this round!')
            break
        input('Press Enter to play the next game')
    display_score(wins)

def play_again():
    prompt("Play again? (y or n)")
    answer = input().lower()

    while answer not in ["yes", "y", "n", "no"]:
        prompt("Please enter y or n")
        answer = input().lower()

    return answer in ("y", "yes")


def main():
    while True:
        play_match()
        if not play_again():
            break

main()
