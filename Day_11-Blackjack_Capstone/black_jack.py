from art import logo
from random import choice, choices

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Functions
def current_scores(user_cards, user_score, computer_card):
    print(f"Your cards: {user_cards}, current score: {user_score}")
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
        computer_hand = [ choice(cards) ]
        # Adjust for double Aces starting hand
        if user_hand_total > 21:
            user_hand[0] = 1
            user_hand_total = add_hand(user_hand)
        current_scores(user_hand, user_hand_total, computer_hand[0])

        # Check for natural Blackjack
        if user_hand_total == 21:
            final_scores(user_hand, user_hand_total, computer_hand, computer_hand[0])
            print(f"Win with a Blackjack \U0001f60E")
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
                        print(f"You went over. You lose \U0001f62d")
                        return play_game()
                    else:
                        first_eleven = user_hand.index(11)
                        user_hand[first_eleven] = 1
                current_scores(user_hand, user_hand_total, computer_hand[0])
            else:
                user_turn = False

        # Computer Draws card
        computer_hand.append(choice(cards))
        computer_hand_total = add_hand(computer_hand)
        # Check for computer having two Aces
        if computer_hand_total > 21:
            computer_hand[0] = 1
            computer_hand_total = add_hand(computer_hand)
        while computer_hand_total < 17:
            computer_hand.append(choice(cards))
            computer_hand_total = add_hand(computer_hand)
            while computer_hand_total > 21:
                if 11 not in computer_hand:
                    final_scores(user_hand, user_hand_total, computer_hand, computer_hand_total)
                    print(f"Opponent went over. You win \U0001f601")
                    return play_game()
                else:
                    first_eleven = computer_hand.index(11)
                    computer_hand[first_eleven] = 1

        # Game Ends
        final_scores(user_hand, user_hand_total, computer_hand, computer_hand_total)
        if computer_hand_total == 21:
            print(f"Lose, opponent has Blackjack \U0001f631")
        elif computer_hand_total > user_hand_total:
            print(f"You lose \U0001f624")
        elif computer_hand_total == user_hand_total:
            print(f"Draw \U0001f643")
        else:
            print(f"You win \U0001f603")
        continue_game = False

    return play_game()

play_game()