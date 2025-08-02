import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = len(chosen_word) * "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = set()

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    if len(guessed_letters) > 0:
        print(f"Previous guesses: {guessed_letters}")

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}!YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    guessed_letters.add(guess)
    print(stages[lives])
