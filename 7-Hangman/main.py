import random

from hangman_art import stages, logo
from hangman_words import word_list


end_of_game = False
lives = 0


chosen_word = random.choice(word_list)
display_word = ["_" for letter in chosen_word]

print(logo)
print(f'Pssst, the solution is {chosen_word}.')
print(display_word)
print(stages[lives])

users_past_guesses = []
while not end_of_game:
    guess = input("Guess a letter ").lower()
    if guess in users_past_guesses:
        print(f"You already tried the letter {guess}.")
    else:
        users_past_guesses.append(guess)
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display_word[index] = letter
    else:
        lives += 1

    print(display_word)
    print(stages[lives])

    if "_" not in display_word:
        end_of_game = True
        print("You win!")
    elif lives == 6:
        end_of_game = True
        print("You lose!")


