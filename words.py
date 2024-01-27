#We need this for the mode select prior to running the game
import sys
import os
# importing from the file Game.py
from Game  import *
#importing from the StringDatabse.py
from StringDatabase  import *
#importing from the Guess.py
from Guess import *


def main():
    # this takes care of the modes in the command line
    try:
        mode = sys.argv[1]
    #if no mode is provided
    except IndexError:
        print("Please provide a valid mode: Test or Play")
        sys.exit()
    #if the mode is not play or test 
    if mode.lower() != "test" and mode.lower() != "play":
        print("The mode is not valid. Try again")
        sys.exit()
    #The game keeps being prompted until someone quits via q 
    while True:
        # calling the above method to generate a word
        current_word = picking_word()
        play(mode, current_word)

# This executed the main() function when this file is executed as the running program
if __name__ == "__main__":
    main()