import random
letters = []

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
    print(secret_word)
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
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
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

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    string = ""
    for letter in secret_word:
        for index, letter_1 in enumerate(letters_guessed):
            if letter == letter_1:
                string += letter_1
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
    #TODO: check if the letter guess is in the secret word
    i = 0
    while i < len(secret_word) and guess != secret_word[i]:
        i += 1
    if guess == secret_word[i]:
        return True
    else:
        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while True:
        input_letter = input("Please enter a letter: ")
        if len(input_letter) > 1:
            print("Please enter one letter at a time.")
        elif len(input_letter) == 0:
            print("You did not enter a letter.")
    # #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        else:
            if is_guess_in_word(input_letter, secret_word):
                print("Your guess is in the secret word!")
                guessed_word = get_guessed_word(secret_word, input_letter)
                print(guessed_word)
                if is_word_guessed(secret_word, guessed_word):
                    print("You won!")
                    return False
            if is_guess_in_word(input_letter, secret_word) == False:
                print("Your guess is not in the secret word! Try again.")
    return True
    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost


def test():
    print(get_guessed_word("u", "uyun"))
    print(is_guess_in_word("i", "uyen"))
    print(is_word_guessed("uyei", "uyen"))
test()

#These function calls that will start the game
secret_word = load_word()
print(secret_word)
spaceman(secret_word)
