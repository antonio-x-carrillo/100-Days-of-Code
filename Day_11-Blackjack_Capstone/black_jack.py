from art import logo
from random import choice, choices

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Functions
def current_scores(user_cards, user_score, computer_card):
    print(f"Your cards: {user_cards}, current score:{user_score}")
    print(f"Computer's first card: {computer_card}")

def final_scores(user_cards, user_score, computer_cards, computer_score):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

def add_hand(player_hand):
    hand_total = 0
    for card in player_hand:
        hand_total += card
    return hand_total

def play_game():
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == 'y':
        continue_game = True
    else:
        return print("Thank you for playing!!!")

    while continue_game:
        print(logo)
        user_hand = choices(cards, k=2)
        user_hand_total = add_hand(user_hand)
        computer_hand =  [ choice(cards) ]
        # Adjust for double Aces starting hand
        if user_hand_total > 21:
            user_hand[0] = 1
            user_hand_total = add_hand(user_hand)
        current_scores(user_hand, user_hand_total, computer_hand[0])

        # Check for natural Blackjack
        if user_hand_total == 21:
            final_scores(user_hand, user_hand_total, computer_hand, computer_hand[0])
            print(f"Win with a Blackjack \N{smiling face with sunglasses}")
            return play_game()

        # Prompt for additional user inputs & check for user bust
        user_turn = True
        while user_turn:
            draw_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_cards == 'y':
                user_hand.append(choice(cards))
                user_hand_total = add_hand(user_hand)
                while user_hand_total > 21:
                    if 11 not in user_hand:
                        final_scores(user_hand, user_hand_total, computer_hand, computer_hand[0])
                        print(f"You went over. You lose \N{loudly crying face}")
                        return play_game()
                    else:
                        first_eleven = user_hand.index(11)
                        user_hand[first_eleven] = 1
                current_scores(user_hand, user_hand_total, computer_hand[0])
            else:
                user_turn = False

        # Computer's turn
        # Computer Draws card

        # TODO 8 - Check for computer total under 17
        # TODO 9 - Check for computer bust
        # TODO 10 - Check for ties
        # TODO 11 - Check for player losing
        # TODO 12 - Make all emojis unicode

        # Remaining messages
        print(f"Lose, opponent has Blackjack \N{face screaming in fear}")
        print(f"You lose \U0001f624")
        print(f"Draw \N{upside-down face}")
        print(f"Opponent went over. You win \U0001f601")
        print(f"You win \U0001f603")

        continue_game = False

    return play_game()

play_game()