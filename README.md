# The Great Guessing Game

Welcome to "The Great Guessing Game," a Python application that challenges you to guess a 4-letter word. The game comes with a vast database of over 4000 4-letter English words for an authentic guessing experience.

## How to Play

### Game Modes

1. **Play Mode:** 
   - You try to guess the word without any hints.
   - Command: `python3 words.py play`

2. **Test Mode:**
   - Displays the word that has been randomly chosen, aiding in development and grading.
   - Command: `python3 words.py test`

### Game Features

- **Clear Screen:** When the game starts, the screen is cleared, and the menu appears at the top.

- **Game Title:** "The Great Guessing Game" is displayed prominently.

- **Current Guess:** The current guess is initially displayed as '----' since no letters have been guessed.

- **Letters Guessed:** Displays the letters already guessed by the user to avoid confusion.

- **Options:**
   a. **Guess:** Attempt to guess the word directly.
   b. **Tell me:** Give up and reveal the correct word.
   c. **Letter:** Select an individual letter that might be in the word.
   d. **Quit:** End the game session and display a final report.

- **Cursor:** The cursor awaits your option selection.

### Game Options

1. **Guess Option:**
   - In play mode, you can directly guess the entire word.
   - In test mode, this option is available, but the correct word is shown after your attempt.

2. **Tell Me Option:**
   - You can give up and request the game to reveal the correct word.
   - In test mode, the correct word is always displayed.

3. **Letter Option:**
   - Select an individual letter that might be in the word.
   - If the letter is correct, it will be revealed in the current guess.
   - If incorrect, the letter will be added to the "Letters Guessed" list.

4. **Quit Option:**
   - End the game session and display a final report.

## Running the Game

To play the game, use the following command line options:

- For Play Mode: `python3 words.py play`
- For Test Mode: `python3 words.py test`

## Final Report

After quitting the game, a final report will be displayed, summarizing your performance.

Enjoy "The Great Guessing Game"! Good luck with your word-guessing skills!
