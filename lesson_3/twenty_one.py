import random 
import os

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['H', 'D', 'S', 'C']
DECK = [[suit, value] for suit in SUITS for value in VALUES]

def prompt(message):
    print(f'==> {message}')
    

def initialize_deck():
    deck = [f'{value}{suit}' for suit in SUITS for value in VALUES] 
    random.shuffle(deck)
    return deck

    
def total(cards):
    values = [card[0] for card in cards]

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

def busted(cards):
    return total(cards) > 21

def display_hand(cards):
    return ', '.join(cards)

def player_turn(deck, player_cards):
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
            prompt(f'Your cards are: {display_hand(player_cards)}')
            prompt(f'Your total value is {total(player_cards)}')
        if busted(player_cards):
            break

def dealer_turn(deck, dealer_cards):
    while True:
        if total(dealer_cards) >= 17 or busted(dealer_cards):
            break
        deal(deck, dealer_cards)
    if busted(dealer_cards):
        prompt('The dealer bust. You win!')


def deal(deck, cards):
      cards.append(deck.pop())
    
def deal_starting_cards(deck, player_cards, dealer_cards):
    for i in range(2):
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())
    prompt(f'The dealer\'s cards are: ?, {dealer_cards[1]}')
    prompt(f'Your cards are: {display_hand(player_cards)}')
    prompt(f'Your total card value is: {total(player_cards)}')

def calculate_results(player_cards, dealer_cards):
    dealer_total = total(dealer_cards)
    player_total = total(player_cards
                         )
    os.system('clear')
    if busted(player_cards):
        prompt('Busted! Dealer wins')
    elif busted(dealer_cards):
        prompt('You win! Dealer busted.')
    elif player_total > dealer_total:
        prompt('You win!')
    elif player_total < dealer_total:
        prompt('Dealer wins!')
    else:
        prompt('Tie game!')

    display_results(player_cards, dealer_cards)

def display_results(player_cards, dealer_cards):
    prompt(f'Your cards are: {display_hand(player_cards)} with a total value of {total(player_cards)}')
    prompt(f'The dealer\'s cards are: {display_hand(dealer_cards)} with a total value of {total(dealer_cards)}')


def play_twenty_one():
    os.system('clear')
    current_deck = initialize_deck()
    player_cards = []
    dealer_cards = []
    deal_starting_cards(current_deck, player_cards, dealer_cards)
    
    player_turn(current_deck, player_cards)

    if not busted(player_cards):
        dealer_turn(current_deck, dealer_cards)
    
    calculate_results(player_cards, dealer_cards)

def play_again():
    prompt("Play again? (y or n)")
    answer = input().lower()

    while answer not in ["yes", "y", "n", "no"]:
        prompt("Please enter y or n")
        answer = input().lower()

    return answer in ("y", "yes")

def main():
    while True:
        play_twenty_one()
        if not play_again():
            break


main()



    



