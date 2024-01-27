#Needed to import this to use the random
import random


# this is the function to pick a random word  from the four_letters.txt
def picking_word():
    try:
        with open("four_letters.txt", 'r') as file:
            content = file.read()
            words = content.split()  # Split the content into a list of words
            if words:
                random_word = random.choice(words).lower()
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("File  is not found.")
    return random_word
