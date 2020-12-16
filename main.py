import random
from Class_Hangman import play
from Class_files.Player import player as pl
"""
Name: Scott Andrew Son  
Class: CIS189
Program language: python

Program: Hangman game 

This program runs a command console game of hangman. It will take a list of words from a text document given. 
store those words in an array. 
It will then randomly pick an element from that array and that would be the word the player will get. 
The player will loop the game until the player decides to quit.
When the player quits it will return back to the console players name, wins, loss, and percentage of games won.

"""


def get_list():  # gets words from text file into the list
    with open("1000_words.txt") as txt_file:  # opens the text file that has 1000 words
        wl = [line.rstrip() for line in txt_file]  # this stores each line into a list
    return wl


def get_word(wl):  # gets random word from list
    word = random.choice(wl)
    return word.upper()


def win_loss(wins, games_played):  # returns percentages
    percent = float(wins / games_played)
    return "win percentage: {:.0%}".format(percent * 100)


def main():  # plays the game
    wl = get_list()
    wins = 0  # wins variable
    loss = 0  # loss Variable
    game_count = 1
    name = str(input("What is your name? "))  # gets name of user and sets it to the variable
    player = pl(name)  # sets player class
    print(player.display())  # displays player class before running the game
    while input("play hangman? (y/n)").upper() == "Y":  # Loop of the game
        word = get_word(wl)
        guessed = play(word)
        # these decision statements will add to either wins or losses depending on how the game goes.
        if guessed:
            wins += 1
            print("Great you guessed the word ", word, ".\n")
            player.update_wins(wins)
        else:
            loss += 1
            print("Sorry the word was ", word, ".\n")
            player.update_loss(loss)
        game_count += 1

    print(player.display(), win_loss(wins, game_count))  # displays win and losses
    print(player.__str__())  # returns the string data
    print(player.__repr__())  # returns the repr data


if __name__ == "__main__":
    main()
