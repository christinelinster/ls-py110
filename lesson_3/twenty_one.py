import random 
import os

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['H', 'D', 'S', 'C']
DECK = [[suit, value] for suit in SUITS for value in VALUES]

def prompt(message):
    print(f'==> {message}')
    

def shuffle(deck):
    random.shuffle(deck)
    return deck

    
def total(cards):
    values = [card[1] for card in cards]

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
    if total(cards) > 21:
        return True
    return False

def display_hand(cards):
    prompt(cards)
    prompt(f'The total value is: {total(cards)}')

def player_turn(deck, player_cards):
    while True:
        answer = input('hit or stay?: ')
        os.system('clear')
        if answer == 'stay' or busted(player_cards):
            break
        
        deal(deck, player_cards)
        display_hand(player_cards)
        if busted(player_cards):
            break

    if busted(player_cards):
        prompt('Bust! You lost!')
    else: 
        prompt('You chose to stay!')

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
    prompt(f'Dealer cards: ?, {dealer_cards[1]}')
    display_hand(player_cards)

def calculate_results(player_cards, dealer_cards):
    os.system('clear')
    if not busted(player_cards) and not busted(dealer_cards):
        if total(player_cards) > total(dealer_cards):
            prompt('Player won!')
        elif total(dealer_cards) > total(player_cards):
            prompt('You lose!')
    elif busted(player_cards) and busted(dealer_cards):
        prompt('Both busted, Tie game!')
    elif busted(player_cards):
        prompt('Busted! Dealer wins')
    elif busted(dealer_cards):
        prompt('You win! Dealer busted.')

    display_results(player_cards, dealer_cards)

def display_results(player_cards, dealer_cards):
    prompt(f'Your cards are: {player_cards}')
    prompt(f'Your total value was: {total(player_cards)}')
    prompt(f'The dealer\'s cards are: {dealer_cards}')
    prompt(f'The dealer\'s total value was: {total(dealer_cards)}')


def play_twenty_one():
    current_deck = shuffle(DECK)
    player_cards = []
    dealer_cards = []
    deal_starting_cards(current_deck, player_cards, dealer_cards)
    player_turn(current_deck, player_cards)

    if busted(player_cards):
        calculate_results(player_cards, dealer_cards)
    else: 
        dealer_turn(current_deck, dealer_cards)
        calculate_results(player_cards, dealer_cards)


play_twenty_one()



    



