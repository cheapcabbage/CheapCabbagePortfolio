# importing random module
import random
# importing word list
import Hangman_words
# importing ascii art
import Hangman_art

# choose random word
chosen_word = Hangman_words.word_list[random.randint(0, len(Hangman_words.word_list) - 1)]
# create var to store chosen_word length
word_length = len(chosen_word)

# create empty list for display with len of chosen word
display = []
# fill display with amount of '_' to match chosen_word
for n in range(word_length):
    display += '_'

# display Hangman logo
print(Hangman_art.logo)
# display the mystery chosen word
print(f"This is your mystery word! {display}")

# create var to store number of lives
lives_left = len(Hangman_art.stages)-1

# print starting drawing (6 starting lives)
print(Hangman_art.stages[lives_left])
# print number of starting lives
print(f"You have {lives_left} lives to start! Good luck girl!")

# print chosen word for testing
print(f"Psst.. your word is {chosen_word}")
# while display still has missing letters or lives > 0 repeat loop
while lives_left > 0 and '_' in display:
    # prompt user for input
    user_input = input("Guess a lowercase letter")
    # if input does not match letter, decrement lives by 1
    if user_input not in chosen_word:  # if user guessed wrong, output statement, decrement lives by 1
        lives_left -= 1
        print(f"Sorry, you suck at guessing! '{user_input}' is not in the word.. You lost a life.")
    elif user_input in display:  # if user already guessed a letter, output statement
        print(f"Is your memory bad, or you just don't know how to read? You already guessed '{user_input}'!")
    # else check if user input matches letter in chosen word
    else:
        for i in range(word_length):
            if user_input == chosen_word[i]:
                # if input matches letter show letter
                display[i] = user_input
                print(f"Good guess! '{user_input}' is in the mystery word!")
    print(f"Your current word is: {display}.")
    print(Hangman_art.stages[lives_left])
    print(f"You have {lives_left} lives left.")
if lives_left == 0 and '_' in display:
    print(f"Sorry, you lost! The correct word was {chosen_word}.")
elif lives_left > 0 and '_' not in display:
    print(f"You win! You had {lives_left} lives left!")

# fix and make it so doesn't repeat output statement for each occurring letter in correct guess
