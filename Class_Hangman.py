from Class_files.graphics import display_hangman as dh

"""
Purpose of function:
Driver game, user completes steps to 
"""


def play(word):
    word_completion = "_" * len(word)  # The amount of "_" for the length of the word chose.
    guessed = False
    guessed_letters = []  # holds the guessed letters
    guessed_words = []  # holds the guessed words
    tries = 6  # Minimum amount of tries.
    print("Lets play hangman")
    print(dh(tries))  # dh is the hangman graphic that is displayed when the game starts and as you guess.
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:  # loops until you're out of guesses or the guessed equals true.
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():  # checks to see if guess is alphabetical
            if guess in guessed_letters:  # checks to see if guessed letter is in the array if so prints out it is already in array and loops back
                print("You already guessed the letter", guess)
                print(guessed_letters)
            elif guess not in word:  # if letter is not in the word it will subtract from tries
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                print(dh(tries))
                print(word_completion)
            else:

                # else you guessed the letter
                print("good job,", guess, "is part of the word")
                print(guessed_letters)
                word_as_list = list(word_completion)
                # gets the word puts it into the a list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # loops to the location of the letters in the word
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                print(dh(tries))
                print(word_completion)
                if "_" not in word_completion:  # if there are no more _ than ends  the loop and guessed changes to true
                    guessed = True
        elif len(guess) == len(
                word) and guess.isalpha():  # this checks if the user guessed a word, checks length and if it is alphabetical
            if guess in guessed_words:
                print("you already guessed the word", guess)
                print(guessed_words)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
                print(dh(tries))
                print(word_completion)
            else:
                guessed = True
                word_completion = word
        else: # else if its not a valid guess it won't be counted against the user
            print("not a valid guess.")
            print(dh(tries))
            print(word_completion)
            print("\n")
    return guessed
