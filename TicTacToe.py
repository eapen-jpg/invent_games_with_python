import random


# ------------- Functions ---------------

def draw_board(board):
    # this function will print the game board, which is numbered like the keyboard's number pad, the player picks a number to tell the game which space they want to move on'''
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] + '     7 | 8 | 9')
    print('---------    -----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + '     4 | 5 | 6')
    print('---------    -----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] + '     1 | 2 | 3')
    print('\n')


def choose_player_letter():
    # the player chooses a letter between X and O, the computer gets the other letter
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose who goes first.
    turn = ''
    if random.randint(0, 1) == 0:
        turn = 'computer'
    else:
        turn = 'player'
    return turn


def make_move(board, letter, move):
    # the player or computer chooses a move on the board
    board[move] = letter


def is_winner(board, letter):
    # Given a board and a player’s letter, this function returns True if that player has won.

    winning_combos = [
        (7, 8, 9), (4, 5, 6), (1, 2, 3),
        (7, 4, 1), (8, 5, 2), (9, 6, 3),
        (7, 5, 3), (9, 5, 1)
    ]

    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c] == letter:
            return True
    return False
    '''
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # Across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or # Across the middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or # Across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or # Down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or # Down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or # Down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or # Diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)) # Diagonal
    '''


def get_board(board):
    """Make a duplicate of the board list and return it the duplicate. The AI algorithm to make temporary modifications to a temporary copy of the board without changing the original board."""
    dupe_board = []
    for i in board:
        dupe_board.append(i)
    return dupe_board


def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def get_player_move(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Move on which space? (1-9)')
        move = input()
    return int(move)


def choose_random_move(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is the algorithm for the Tic Tac Toe AI:
    # First, check if the computer can win in the next move
    for i in range(1, 10):
        copy_board = get_board(board)
        if is_space_free(copy_board, i):
            make_move(copy_board, computer_letter, i)
            if is_winner(copy_board, computer_letter):
                return i
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy_board = get_board(board)
        if is_space_free(copy_board, i):
            make_move(copy_board, player_letter, i)
            if is_winner(copy_board, player_letter):
                return i
    # choose a random move from the corner spaces
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5
    # Move on one of the sides.
    return choose_random_move(board, [2, 4, 6, 8])


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


# ------------ Start Execution -------------

# Play a game of tic tac toe
if __name__ == '__main__':
    # Start game
    print("Let's play a game of tictactoe!\n")

    # the game keeps playing until the execution encounters a break statement
    while True:
        # Reset the board
        # the_board is a list of 10 strings representing the board (ignore index 0)
        the_board = [' '] * 10

        # player chooses letter
        player_letter, computer_letter = choose_player_letter()
        print('Your {}, the computer is {}.\n'.format(player_letter, computer_letter))

        # decide who's first
        turn = who_goes_first()
        print('The ' + turn + ' has been randomly chosen to go first')

        # keep track of if game is still playing
        game_is_playing = True

        while game_is_playing:
            if turn == 'player':
                # it's the player’s turn
                # display board
                draw_board(the_board)

                # player decides their move
                move = get_player_move(the_board)

                # player's move is displayed on the board
                make_move(the_board, player_letter, move)

                # check if player is winner
                if is_winner(the_board, player_letter):
                    draw_board(the_board)
                    print('Hooray! You Win!!!')
                    game_is_playing = False
                else:
                    # check if it's a tie
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # it's the computer’s turn
                # the computer decides their move
                move = get_computer_move(the_board, computer_letter)

                # computer's move is displayed on the board
                make_move(the_board, computer_letter, move)

                # check if the computer is winner
                if is_winner(the_board, computer_letter):
                    draw_board(the_board)
                    print('Oh no! The computer has won. You Lose.')
                    game_is_playing = False
                else:
                    # check if it's a tie
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        # it's the player's turn
                        turn = 'player'

        # check if the player wants to play again
        print('Do you want to play again? (yes or no)')

        if not input().lower().startswith('y'):
            break