import random

HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 ==========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |a
   O   |
  /|\  |
  / \  |
       |
 =========''']

# Create a nice list of words which the player can guess
words = 'ant'.split()


# Define functions
def getRandomWord(wordList):
    # Returns a random string from the list of words
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_ ' * len(secretWord)

    for i in range(len(secretWord)):  # Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # Show the secret word with spaces between each letter
        print(letter, end='')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player already entered. This function makes sure that the player entered a single letter.
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('One at a time please!')
        elif guess in alreadyGuessed:
            print('You\'ve already guessed that letter. Try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Stop messing about and type in a LETTER.')
        else:
            return guess


def playAgain():
    # The unemployed amoung us may have enough free time to want another game.
    print('Would you like to play again? (please enter yes or no)')
    return input().lower().startswith('y')


# Initialise the game
print('\n H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # First, prompt the player to type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check for the win condition (guess = secretWord)
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Congratulations! You correctly guessed the secret word: ' + secretWord + '! ' + 'You\'re Winner!')
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # Check for the lose condition (final guess occurs before the player dies)
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print(
                    'You have run out of guesses. You might still be alive if you knew that the secret word was ' + secretWord + '...')
                gameIsDone = True

        # Ask the player if they would like to play again (Requires game to be finished first).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                print('Thanks for playing!')
                break