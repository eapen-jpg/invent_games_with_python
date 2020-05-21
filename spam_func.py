import random

NUM_SIZE = 3
WELCOME_MSG = '''
===============================================================
I am thinking of a 3-digit number. Try to guess what it is.
The clues I give are...
When I say:    That means:
   Bagels      None of the digits is correct.
   Pico        One digit is correct but in the wrong positon.
   Fermi       One digit is correct and in the right position.
I have thought up a number. You have 10 guesses to get it.
==============================================================='''


def bagels():
    '''Main function.'''

    while True:
        print(WELCOME_MSG)
        number = get_number()
        guesses = 0

        while guesses < 10:
            guesses += 1
            guess = get_guess(guesses)
            if win_check(guess, number): break
            if guesses == 10: print(f'It was {number}.')

        # Ask if user would like to play again.
        while True:
            play_again = input('Would you like to play again? (yes or no): ').lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                return


def get_number():
    '''Chooses random number depending on NUM_SIZE.'''

    number = ''
    numbers = list(range(10))
    random.shuffle(numbers)

    for i in range(NUM_SIZE): number += str(numbers[i])

    return number


def get_guess(guesses):
    '''Asks user for input until it is valid and returns it.'''

    while True:
        guess = input(f'Guess #{guesses}:\n')
        # Check if the input contains only digits and is NUM_SIZE long.
        if len(guess) != NUM_SIZE or not guess.isdigit():
            print(f'Your guess must be {NUM_SIZE} digit long and contain only digits.')
            continue

        # Check if every digit is different from other.
        same_digits = False
        for i in range(NUM_SIZE - 1):
            for j in range(i + 1, NUM_SIZE):
                if guess[i] == guess[j]: same_digits = True
        if not same_digits: return guess
        print("Every digit must be different.")


def win_check(guess, number):
    '''Returns true if user guessed the number, else prints tips and returns false.'''

    if guess == number:
        print('You got it!')
        return True

    # Print tips.
    tips = []

    for guess_id, guess_digit in enumerate(guess):
        for number_id, number_digit in enumerate(number):
            if guess_digit == number_digit and guess_id == number_id:
                tips.append('Fermi')
            elif guess_digit == number_digit:
                tips.append('Pico')

    if not tips:
        print('Bagels')
        return False

    tips.sort()
    print(' '.join(tips))

    return False


if __name__ == "__main__":
    bagels()