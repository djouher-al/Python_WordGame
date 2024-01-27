#Needed to import this for the clear function
import os

#This is the constructor for the game objects 
class Game:
    def __init__(self, letter_guessed, status, current_word, bad_guesses, missed_letters, score):
        self.letter_guessed = letter_guessed
        self.status= status
        self.current_word = current_word
        self.bad_guesses= bad_guesses
        self.missed_letters= missed_letters 
        self.score = score

# This is a list that stores all the game objects 
all_games = []

#This is our dictionnary of the frequences for each letter
my_dict = {"a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.7,
            "f": 2.23, "g": 2.02, "h": 6.09, "i":6.97, "j": 0.15,
            "k": 0.77, "l":4.03, "m":2.41, "n":6.75, "o":7.51,
            "p": 1.93, "q":0.10, "r":5.99, "s":6.33, "t":9.06,
            "u": 2.76, "v": 0.98, "w": 2.36, "x":0.15, "y":1.97, "z":0.07}


# this is in order to save all the games after someone guesses 
def save_game(letter_guessed, status, current_word, bad_guesses, missed_letters, score):
    global all_games
    # Create an instance of the Game class
    my_game = Game(letter_guessed, status, current_word, bad_guesses, missed_letters, score)
    all_games.append(my_game)

#This calculate the number of missed letters 
def calculate_missed_letters(letter_guesses, current_word):
    total_missed_letters = 0
    for letter in letter_guesses:
        if letter not in current_word:
            total_missed_letters += 1
    return total_missed_letters


# This calculates the points for each "-" and devided it by the  missed  letters
def calculate_score(word_in_progress, current_word, missed_letters):
    score=0
    points_added =0
    for letter in  current_word:
        if letter not in word_in_progress:
            points_added += my_dict.get(letter, 0)
    #otherwise it will devide it by zero
    if(missed_letters==0):
        score = (score+ points_added)
    else:
        score = (score+ points_added)/ missed_letters
    return score


# If a user gives up via t, this calculates the points of each "-"/ not guessed by their frequencies 
def calculate_give_up(word_in_progress, current_word):
    points_removed = 0
    for letter in  current_word:
        if letter not in word_in_progress:
            points_removed -= my_dict.get(letter, 0)
    return points_removed

# This function calculates the score based on if t or g 
def game_total_score(word_in_progress,current_word, option, bad_guesses, missed_letters):
    # calculate_give_up is used to calculate the negative score 
    if option == "t":
        # When we give up, we loose points for each uncovered letter
        total_score = calculate_give_up(word_in_progress, current_word)
    else:
         # we would loose 10% each time of our final score for each bad guesses, 
         # we win points for a good guess based on the uncovered letter. The total is devided by the # of missed letters 
        total_score = (1-(bad_guesses* 0.10))* (calculate_score(word_in_progress, current_word, missed_letters))
    #The round is used here to round to 2 sign.number 
    return round(total_score,2)

# this function clears the screen, depending if the OS is Mac or Windows 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Ths function is used to print the report of the games played 
def display_games():
    global all_games
    final_score = 0 
    #clear the screen
    clear_screen()
    # Display the instance variables for each game in the global list
    print("++")
    print("++ Game Report")
    print("++\n")
    print(f"{'Game':<8}{'Word':<8}{'Status':<12}{'Bad Guesses':<20}{'Missed Letters':<25}{'Score'}")
    print(f"{'----':<8}{'----':<8}{'--------':<12}{'-----------':<20}{'--------------':<25}{'-----'}")
    #printing for each game the info
    for i, game in enumerate(all_games):
        print(f"{i + 1:<8}{str(game.current_word):<8}{str(game.status):<12}{str(game.bad_guesses):<20}{str(game.missed_letters):<25}{str(game.score)}")
        final_score += game.score
    # Printing final score here     
    print("\nFinal Score: ", round(final_score,2))