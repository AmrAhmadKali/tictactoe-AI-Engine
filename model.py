"""This module serves as model Element in an MVC Architecture"""
import copy
import numpy
import json

DIMENSION = 3


def new_board():
    """A method to return an empty board"""
    return [[None, None, None], [None, None, None], [None, None, None]]


def is_valid_move(board, coordinate) -> bool:
    """A method to check if a specific move is valid or not"""
    if board[coordinate[0]][coordinate[1]] is None:
        return True
    return False


def player(board, first_player):
    """A method to give back which player is on and to always flip between x
     and o every round
    """
    x_plays = 0
    o_plays = 0
    for line in board:
        for cell in line:
            if cell == "x":
                x_plays += 1
            elif cell == "o":
                o_plays += 1

    if x_plays - o_plays == 1:
        return 'o'

    elif o_plays - x_plays == 1:
        return 'x'

    return first_player


def make_move(board, coordinate, player_symbol):
    """A method to execute a specific move on the board and give the board back"""
    updated_board = copy.deepcopy(board)
    updated_board[coordinate[0]][coordinate[1]] = player_symbol
    return updated_board


def save_game(board, first_player, mode):
    """A method to save the state of the game at any point of time"""
    # \ (backslash) for windows systems, not sure about compatibility in Linux based OS
    with open("data\\board.json", "w") as board_file:
        json.dump(board, board_file)

    with open("data\\player.json", "w") as player_file:
        json.dump(first_player, player_file)

    with open("data\\mode.json", "w") as mode_file:
        json.dump(mode, mode_file)


def load_game():
    """A method to load the state of the game if the last game is not terminated"""
    board = None
    first_player = None
    with open("data\\board.json", "r") as board_file:
        board = json.load(board_file)

    with open("data\\player.json", "r") as player_file:
        first_player = json.load(player_file)

    with open("data\\mode.json", "r") as mode_file:
        mode = json.load(mode_file)

    return board, first_player, mode


# @profile
def get_winner(board):
    """A method to determine which is the winner if any at a specific point of time"""
    transposed_board = numpy.transpose(board)
    for row in range(DIMENSION):
        if board[row] == 3 * ['x']:  # If any row are just Xs
            return 'x'

        elif board[row] == 3 * ['o']:  # If any row are just Os
            return 'o'

        elif all(transposed_board[row] == 3 * ['x']):  # If any Column are just Xs      might need all()   ##ToWorkOn
            return 'x'

        elif all(transposed_board[row] == 3 * ['o']):  # If any Column are just Os      might need all()   ##ToWorkOn
            return 'o'

    main_diagonal = numpy.diagonal(board)

    counter_diagonal = numpy.fliplr(board).diagonal()

    if all(main_diagonal == (3 * ['x'])):  # If diagonal is just Xs
        return 'x'

    elif all(counter_diagonal == (3 * ['x'])):  # If diagonal is just Xs
        return 'x'

    elif all(main_diagonal == 3 * ['o']):  # If diagonal is just Os
        return 'o'

    elif all(counter_diagonal == (3 * ['o'])):  # If diagonal is just Os
        return 'o'

    return False


def is_full(board):
    """A method to check if the board is full at a specific point of time"""
    for row in board:
        for cell in row:
            if cell is None:
                return False

    return True
