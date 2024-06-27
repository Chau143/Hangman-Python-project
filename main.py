import random
import string

# Sample words list (since `words` module/data is not provided)
words = ["python", "java", "kotlin", "javascript"]

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    attempts = 6  # number of attempts the player has

    while len(word_letters) > 0 and attempts > 0:
        # Display current state
        print('You have', attempts, 'attempts left and have used these letters:', ' '.join(used_letters))

        # Display current word with guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good guess! {user_letter} is in the word.")
            else:
                attempts -= 1
                print(f"Wrong guess! {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # Game over
    if attempts == 0:
        print(f"Sorry, you lost! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word} correctly!")

hangman()