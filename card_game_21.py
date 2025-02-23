# Card Game 21 Module File
#
from collections import namedtuple
from random import shuffle, seed, randint
from time import time

# skills and concepts
#
#   ASCII art
#   strings
#   formatting
#   lists
#   TUPLES
#   SETS
#   branching/decisions
#   looping/repetion
#   functions
#   unit testing



# cards have width 12 characters
# cards have height 10 lines

# ' ---------- '  ' ---------- '  ' ---------- '  ' ---------- '  line 0  
# '|10        |'  '|5         |'  '|8   __    |'  '|2         |'  line 1
# '|♥  _  _   |'  '|♦   /\    |'  '|♣  /  \   |'  '|♠   /\    |'  line 2
# '|  / \/ \  |'  '|   /  \   |'  '|  _\  /_  |'  '|   /  \   |'  line 3
# '| |      | |'  '|  /    \  |'  '| |      | |'  '|  /    \  |'  line 4
# '|  \    /  |'  '|  \    /  |'  '| \_/\/\_/ |'  '|  \_  _/  |'  line 5
# '|   \  /   |'  '|   \  /   |'  '|    ||    |'  '|    ||    |'  line 6
# '|    \/   ♥|'  '|    \/   ♦|'  '|   /__\  ♣|'  '|   /__\  ♠|'  line 7
# '|        10|'  '|         5|'  '|         8|'  '|         2|'  line 8
# ' ---------- '  ' ---------- '  ' ---------- '  ' ---------- '  line 9

#     heart          diamond         club            spade
#     example        example         example         example


# ' ---------- '  ' ---------- '  ' ---------- '  ' ---------- '  line 0
# '|A         |'  '|J         |'  '|Q         |'  '|K         |'  line 1
# '|S         |'  '|S  ___    |'  '|S   ___   |'  '|S         |'  line 2
# '|    /\    |'  '|      |   |'  '|   /   \  |'  '|   |  /   |'  line 3
# '|   /__\   |'  '|      |   |'  '|  |     | |'  '|   |_/    |'  line 4
# '|  |    |  |'  '|      |   |'  '|  |     | |'  '|   |  \   |'  line 5
# '|  |    |  |'  '|  \___/   |'  '|   \___X  |'  '|   |   \  |'  line 6
# '|         S|'  '|         S|'  '|         S|'  '|         S|'  line 7
# '|         A|'  '|         J|'  '|         Q|'  '|         K|'  line 8
# ' ---------- '  ' ---------- '  ' ---------- '  ' ---------- '  line 9

# replace the letter S with a suit symbol


# -------------------------------------------------------------------

# ASCII 9824 Spades
# ASCII 9827 Clubs
# ASCII 9829 Hearts
# ASCII 9830 Diamonds

SUITS = '♣♦♥♠'    # do not modify

CLUB    = '♣'     # do not modify
DIAMOND = '♦'     # do not modify
HEART   = '♥'     # do not modify
SPADE   = '♠'     # do not modify

# These values are useful for sorting.
# They are NOT the values the cards have in the game 21.
VALUES = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]          # do not modify

RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']  # do not modify


# game state data

card_deck = set([])  # do not modify this line
dealer_cards = []    # do not modify this line
player_cards = []    # do not modify this line


# ------------------------------------------------------------------
# DO NOT MODIFY ABOVE THIS LINE
# ------------------------------------------------------------------


# Card type
#   suit:  (str) heart symbol, diamond symbol, club symbol, spade symbol
#   value: (int) 1-13  Ace is 1, Jack is 11, Queen is 12, King is 13
#   rank:  (str) A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
#
# suit must be before value for proper sorting
# value must be before rank for proper sorting
#

# TODO - create the Card data type
#Card type
Card = namedtuple('Card',['suit','value','rank'])


# ----------------------------------------------------------------------

# TODO - write the create_card_deck function
def create_card_deck():
    """Creates a deck of 52 unique playing cards."""
    return {Card(suit, value, RANKS[index]) for suit in SUITS for index, value in enumerate(VALUES)}


# ----------------------------------------------------------------------

# IMPORTANT!  
# This function changes the global variable *card\_deck*.  
# 
# IMPORTANT!  
# You should shuffle the card deck by repeatedly removing  
# a card from the deck and then adding that card back in.  
# Try picking a random number between 1 and 52 and then  
# removing and adding that many cards. Remove and add  
# one card at a time.  

# TODO - write the shuffle_card_deck function
from random import randint

def shuffle_card_deck():
    global card_deck
    card_list = list(card_deck)
    shuffle(card_list)
    card_deck = set(card_list)



# ----------------------------------------------------------------------

# HINT: What does the set pop() function do?

# TODO - write the deal_card_to_dealer function
# TODO - write the deal_card_to_player function

def deal_card_to_dealer():
    card = card_deck.pop()
    dealer_cards.append(card)

def deal_card_to_player():
    card = card_deck.pop()
    player_cards.append(card)

# ----------------------------------------------------------------------

# TODO - write the card_to_string function

def card_to_string(card):
    """Returns an ASCII representation of a playing card."""
    return f"""
 ---------- 
|{card.rank:<2}        |
|{card.suit}         |
|    /\    |
|   /__\   |
|  |    |  |
|  |    |  |
|         {card.suit}|
|        {card.rank}|
 ---------- 
""".strip()
# ----------------------------------------------------------------------

# HINT:
# To create ASCII art cards arranged horizontally,
# first split each card's ASCII art string at the newline characters.
# Now you have a list of line strings for each card.# 
# print line 0 for each card
# print line 1 for each card
# print line 2 for each card
# ...
# print line 9 for each card

# TODO - write the print_cards function

def print_cards(cards, compact=False, face_up=True):
    """Prints a list of cards in either compact form or ASCII format."""
    if not face_up:
        for _ in cards:
            print(
                ' ---------- \n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                '|XX XX XX XX|\n'
                ' ---------- '
            )
    else:
        card_lines = [card_to_string(card).split("\n") for card in cards]
        for i in range(len(card_lines[0])):
            print("  ".join(card[i] for card in card_lines))





   
# ----------------------------------------------------------------------

# TODO - write the init_game_21 function
def init_game_21():
     global card_deck, dealer_cards, player_cards
     card_deck = create_card_deck()
     shuffle_card_deck()
     dealer_cards = []
     player_cards = []
     deal_card_to_dealer()
     deal_card_to_player()
     deal_card_to_dealer()
     deal_card_to_player()

# ----------------------------------------------------------------------


# HINT: Adds up card total for the 21 card game
# This is NOT a simple total of card values.

# TODO - write the total_cards_for_21 function

def total_cards_for_21(cards):
    """Calculates the best possible total value for a hand in 21."""
    total, total2 = 0, 0
    num_aces = 0

    for card in cards:
        if card.value == 1:  # Ace
            total += 1
            total2 += 11
            num_aces += 1
        elif card.value >= 10:  # Face cards (J, Q, K)
            total += 10
            total2 += 10
        else:
            total += card.value
            total2 += card.value

    while num_aces > 0 and total2 > 21:
        total2 -= 10
        num_aces -= 1

    return total, total2  # Ensure it always returns two values




# ======================================================================

#############################################
#                                           #
#      DO NOT MODIFY BELOW THIS LINE        #
#                                           #
#############################################


CONTINUE_GAME = 0  # do not modify this line
PLAYER_WON    = 1  # do not modify this line
DEALER_WON    = 2  # do not modify this line
GAME_TIED     = 3  # do not modify this line

# DO NOT MODIFY THIS FUNCTION
#
def play_one_turn_21( compact = False ):
    '''
    Plays one turn of the 21 card game.
    The goal is to get close to 21 without going over.

    parameters: compact (boolean) - optional parameter, default False
                           True - cards are printed in compact form
                           False - cards are ASCII art (default)

    returns: (int) returns the game result, one of the following
              CONTINUE_GAME, PLAYER_WON, DEALER_WON, GAME_TIED
    '''

    print( '===========================================================\n' )

    # What does the dealer want to do?
    # --------------------------------

    # dealer's current total (total: Ace is 1pt, total2: Ace is 11pts)

    dealer_total, dealer_total2 = total_cards_for_21( dealer_cards )

    # dealer gets another card?

    dealer_max = 18   # dealer will not ask for more cards above max total
                      # unless player has already revealed cards and has
                      # 18 or more
                      
    dealer_got_new_card_text = ''

    dealerWillRiskBusting = False
    a,b = total_cards_for_21( player_cards )
    if b > 18 and b <= 21:
        dealerWillRiskBusting = True
    
    if (dealer_total < dealer_max and dealer_total2 != 21) or dealerWillRiskBusting:
        
        print( "dealer's cards: ", end='' )
        if not compact: print( '\n' )
        print_cards( dealer_cards, compact, face_up=False )
        
        deal_card_to_dealer()
        dealer_total, dealer_total2 = total_cards_for_21( dealer_cards )
        if dealer_total2 > dealer_total: dealer_total = dealer_total2

        dealer_got_new_card_text = ' after hit'
        
        print( "dealer hits" )
        if not compact: print( '' )

    # dealer sticks? busts?

    dealer_busts = False
    dealer_sticks = False
    
    if dealer_total >= dealer_max or dealer_total2 == 21:
        dealer_total = max( dealer_total, dealer_total2 )
        if dealer_total > 21:
            dealer_busts = True
            #print( "dealer busts" )
        #else:
        #    print( "dealer sticks" )
        #    if not compact: print( '' )
        dealer_sticks = True

    # print dealer's cards

    print( "dealer's cards" + dealer_got_new_card_text + ": ", end='' )
    if not compact: print( '\n' )
    
    print_cards( dealer_cards, compact, face_up=dealer_sticks )

    if dealer_busts:
        print( "dealer busts\n" )
    elif dealer_sticks:
        print( "dealer sticks\n" )


    print( '===========================================================\n' )

    # What does the player want to do?
    # --------------------------------

    # player's current total (total: Ace is 1pt, total2: Ace is 11pts)

    player_total, player_total2 = total_cards_for_21( player_cards )
    if player_total2 == 21:
        player_total = player_total2

    # print player's cards

    print( "player's cards: ", end='' )
    if not compact: print( '\n' )
    
    print_cards( player_cards, compact )

    # automatic stick if player total >= 21 or if dealer busted

    player_sticks = False
    
    if player_total > 21:

        print( "player busts\n" )
        player_sticks = True

    elif player_total == 21 or dealer_busts:
        
        print( "player sticks\n" )
        player_sticks = True
    
    else:
        # ask player, hit or stick?
     
        answer = input("hit or stick? (h/s): ").lower()
        if len(answer) > 1: answer = answer[0]
        while answer != 'h' and answer != 's':
            answer = input("hit or stick? (h/s): ").lower()
            if len(answer) > 1: answer = answer[0]

        if answer == 's':
            print( "player sticks\n" )
            player_sticks = True
    
        else:
            deal_card_to_player()
            player_total, player_total2 = total_cards_for_21( player_cards )
            if player_total2 > player_total: player_total = player_total2
            print( "player hits\n" )

            print( "player's cards after hit: ", end='' )
            if not compact: print( '\n' )

            print_cards( player_cards, compact )

            if player_total > 21:
                print( 'player busts\n' )
                player_sticks = True
            elif player_total == 21:
                print( 'player sticks\n' )
                player_sticks = True


    # What is the result of this game turn?
    # -------------------------------------

    # no one busted, don't yet have both sticking
    if (dealer_total < 21 and player_total < 21) \
                        and False == (dealer_sticks and player_sticks):
        return CONTINUE_GAME

    # no one sticks
    #if False == dealer_sticks and False == player_sticks:
    #    return CONTINUE_GAME

    # report scores
    dealer_busted = '(busted)' if dealer_total > 21 else ''
    player_busted = '(busted)' if player_total > 21 else ''
    print( "dealer total:", dealer_total, dealer_busted )
    print( "player total:", player_total, player_busted )
    print( '' )

    # both have same score
    if player_total == dealer_total:
        print( "game tied (same score)\n" )
        return GAME_TIED

    # both busted
    if player_total > 21 and dealer_total > 21:
        print( "game tied (both busted)\n" )
        return GAME_TIED

    # player busted
    if player_total > 21:
        print( "dealer wins\n" )
        return DEALER_WON

    # dealer busted
    if dealer_total > 21:
        print( "PLAYER WINS!!!\n" )
        return PLAYER_WON

    # whoever is closer to 21 without going over won
    if player_total > dealer_total:
        print( "PLAYER WINS!!!\n" )
        return PLAYER_WON
    else:
        print( "dealer wins\n" )
        return DEALER_WON

    print( "ERROR: game logic error, this line should never execute\n" )

    return GAME_TIED

# ----------------------------------------------------------------------

# DO NOT MODIFY THIS FUNCTION
#
def print_instructions_21():
    '''
    Prints instructions for the card game 21.

    no parameters

    returns: (boolean) cards should be compact
             True - cards should be displayed in compact form
             False - cards should be displayed as ASCII Art
    '''

    print( '' )
    print( "Let's play 21!" )
    print( '' )
    print( 'The goal is to get as close to 21 as possible without going over.' )
    print( 'The winner is determined after both players reveal their cards.' )
    print( '' )
    print( 'Ace - worth 1 point or 11 points, player decides' )
    print( 'face cards - (Jack, Queen, King) worth 10 pts each' )
    print( 'number cards - worth their face value' )
    print( '' )
    print( 'You start with two cards.' )
    print( 'You may take these actions.' )
    print( '  hit - ask for another card' )
    print( '  stick - reveal cards' )
    print( '' )

    compact = True
    answer = input( "ASCII art or compact cards? (a/c): " ).lower()
    if answer == 'a' or answer == '':
        compact = False
    print( '' )

##    print( 'press ENTER to begin' )
##    answer = input()
##    print( '\n' )

    return compact

# ----------------------------------------------------------------------

# DO NOT MODIFY THIS FUNCTION
#
def play_card_game_21( compact = True ):
    '''
    Play the 21 card game!

    parameters: compact (boolean) - are cards displayed in compact form?
                                    True (default) - compact cards
                                    False - ASCII art cards

    returns: (boolean) does the player want to play again?
    '''

    init_game_21()

    turns = 0
    result = play_one_turn_21( compact )
    while result == CONTINUE_GAME and turns < 20:
        result = play_one_turn_21( compact )
        turns += 1

    # play again?

    answer = input( "play again? (y/n): " ).lower()
    if answer == 'y':
        return True
    return False

# ======================================================================
# main program

# DO NOT MODIFY THESE TWO LINES
from time import time
from random import seed, randint


# DO NOT MODIFY THIS MAIN PROGRAM
# This will only run when the program is run as a script,
# not when it is loaded as a module.
#
if __name__ == '__main__':

    seed( time() )

    # compact cards (True) or ASCII art cards (False)?
    compactCards = print_instructions_21()

    # keep playing while player wants to keep playing
    play_again = play_card_game_21( compactCards )
    while play_again:
        play_again = play_card_game_21( compactCards )
