import random
import sys
from termcolor import colored

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    i = 0
    while i < len(secret_word):
        if secret_word[i] != letters_guessed[i]:
            return False
        i+=1
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            string += letter
        else:
            string += "_"
    return string

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #Check if the letter guess is in the secret word
    i = 0
    while i < len(secret_word):
        if guess == secret_word[i]:
            return True
        i += 1
    return False

# For information about removing characters from a string, I read https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-9.php
def remove_letter(str, letter_guessed):
    for index, letter in enumerate(str):
        if letter == letter_guessed:
            str = str[:index] + str[index+1:]
    return str

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    incorrect_guesses = 7
    letters_to_guessed = "abcdefghijklmnopqrstuvwxyz"
    letters_guessed = []

    while True:
        print("----------------------------------------------------------")

        input_letter = input(colored("Please enter a letter: ", "cyan", attrs = ["bold"])).lower()
        if input_letter in letters_to_guessed:
            letters_guessed.append(input_letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)

            if len(input_letter) > 1:
                print(colored("Please enter one letter at a time.", "green"))

            elif len(input_letter) == 0:
                print(colored("You did not enter a letter.", "green"))

            else:
                if is_guess_in_word(input_letter, secret_word):
                    print(colored("Your guess is in the secret word!", "magenta"))
                    if is_word_guessed(secret_word, guessed_word):
                        print(colored("You won!", "red", attrs = ["blink"]))
                        return False

                if is_guess_in_word(input_letter, secret_word) == False:
                    incorrect_guesses -= 1
                    if incorrect_guesses == 0:
                        print(colored("Sorry, your word is not in the secret word!", "magenta"))
                        print(colored("You lost!", "red", attrs = ["blink"]))
                        return False
                    print(colored("Your guess is not in the secret word! Try again.", "magenta"))

        else:
            print(colored("You already guessed this letter.", "blue"))

        print(guessed_word)
        print("You have " + str(incorrect_guesses) + " incorrect guesses left.")
        letters_to_guessed = remove_letter(letters_to_guessed, input_letter)
        print("The letters haven't been yet guessed: " + letters_to_guessed)


def test_is_guess_in_word():
    assert is_guess_in_word("u", "uyen") == True
    assert is_guess_in_word("i", "uyen") == False

def test_is_word_guessed():
    assert is_word_guessed("uyei", "uyen") == False
    assert is_word_guessed("uyen", "uyen") == True

def test_get_guessed_word():
    assert get_guessed_word("uyen", ["u", "e"]) == "u_e_"
    assert get_guessed_word("uyen", ["i", "o"]) == "____"

#These function calls that will start the game
playing = True
while playing:
    secret_word = load_word()
    # print(secret_word)
    letters = ["_"] * len(secret_word)
    print("Welcome to Spaceman Game!")
    print("You have 7 incorrect guesses, please enter one letter per round.")
    spaceman(secret_word)
    print("The secret word is: " + colored(secret_word, attrs=['underline']))
    user_input = input(colored("Do you want to play again? Y/N ", "cyan"))
    if user_input.lower() == "n":
        playing = False
