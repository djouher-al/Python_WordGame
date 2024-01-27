#We are calling all the functions in these files 
from Game  import *
from StringDatabase  import *
from words import *
#This is needed for the sys.exit() for q option
import sys


 # this function is to display the word in progress 
def word_progress(random_word,letters_guessed):
    word_progress= ""
    for letter in random_word:
        if letter in  letters_guessed:
            word_progress += letter
        else:
            word_progress += "-"
        
    return word_progress

# This the logic behind the display of the menu 
def play(mode, current_word):
    letters_guessed = []
    guesses = " "
    bad_guesses = 0
    
    while True:
        #menu display
        print("++")
        print("++ The great guessing game")
        print("++")
        print("\n")
        if mode.lower() == "test":
            print("Current Word: ", current_word)
        print("Current Guess: ", word_progress(current_word, letters_guessed))
        print("letters guessed: ", guesses.join(letters_guessed))
        print("g = guess, t = tell me, l for a letter, and q to quit\n")
        
        # this is for the options at the beginning
        possible_options = ["g", "t", "l", "q"]
        option_valid = False
        option = input("Enter option: ")
        #If the option selected is incorrect, it loops until the user select something that's in possible_options
        while option_valid is False:
            if option in possible_options:
                option_valid = True
            else:
                option = input("Invalid option. Please re-enter: ")
        #If the user gives up
        if option.lower() == "t":
            print("\n@@")
            print("@@ Feedback: You gave up! We were looking for the following word:", current_word)
            print("@@\n")
            status = "Gave Up"
            # We're creating an object game with all the appropriate attributes
            save_game(letters_guessed, status, current_word, bad_guesses, calculate_missed_letters(letters_guessed, current_word),
                      game_total_score(word_progress(current_word, letters_guessed), current_word, option.lower(), bad_guesses,
                                       calculate_missed_letters(letters_guessed, current_word)))
            input("Press any key to continue to continue... ")
            clear_screen()
            break
        #If the user wants to guess the word 
        if option.lower() == "g":
            print("\n")
            word_guess = input("Make your guess: ")
             # We're creating an object game with all the appropriate attributes
            if word_guess == current_word:
                print("\n@@")
                print("@@ Feedback: Congrats! You found the  correct word!")
                print("@@\n")
                #We create a game object
                status = "Success"
                save_game(letters_guessed, status, current_word, bad_guesses, calculate_missed_letters(letters_guessed, current_word),
                          game_total_score(word_progress(current_word, letters_guessed), current_word, option.lower(), bad_guesses,
                                           calculate_missed_letters(letters_guessed, current_word)))
                
                input("Press any key to continue to continue... ")
                clear_screen()
                break
            else:
                #Here, we slected the word in wrong word
                print("\n@@")
                print("@@ Feedback: This wasn't the word we are looking for.")
                print("@@\n")
                input("Press any key to continue to continue... ")
                # This increment bad guesses
                bad_guesses += 1
                clear_screen()
        #This is when the user selects to guess a letter
        if option.lower() == "l":
            letter = input("\nEnter a letter: ")
            #The guessed letter added to guesses, which is used for display
            letters_guessed.append(letter)
            guesses.join(letters_guessed)
            print("\n")
            #if the letter is not in the word
            if letter.lower() not in current_word:
                print("@@")
                print("@@Feedback : This letter is not in the word.")
                print("@@\n")
                input("Press any key to continue to continue... ")
                clear_screen()
            #if the letter is in the word
            else:
                print("@@")
                print("Feedback : You found a letter!")
                print("@@\n")
                input("Press any key to continue to continue... ")
                clear_screen()
        #If we quit, this will simply display the report and terminate 
        if option.lower() == "q":
            display_games()
            sys.exit()
