"""This module serves as controller Element in an MVC Architecture"""

import model
import view
import modelai
from time import sleep


def get_move():
    """A method to takes user move as coordinates x and y where
    both take values from 0 to 2
    """
    while True:
        x_coordinate = int(input('X- Coordinate: '))
        y_coordinate = int(input('Y- Coordinate: '))
        if x_coordinate in range(0, 3) and y_coordinate in range(0, 3):
            break
        else:
            print('Invalid Input! Please enter integers between 0 and 2')
    return x_coordinate, y_coordinate


def play_mode_1():
    """A method to control the play between 2 Players"""
    print('Wellcome in Tic-Tac-Toe 2 Players Mode \n ')
    play_mode = 1
    loaded_game = model.load_game()
    current_board = loaded_game[0]
    first_player = loaded_game[1]

    if not modelai.terminal(loaded_game[0]):
        view.render(current_board)
        sleep(0.7)

    else:
        current_board = model.new_board()
        view.render(current_board)
        sleep(0.7)
        first_player = input('Please enter your play symbol x or o (lower case):')
        while True:
            if first_player != 'x' and first_player != 'o':
                first_player = input('Wrong symbol! Please try again with x or o (lower case):')
            else:
                break

    while True:
        current_player = model.player(current_board, first_player)

        print(f'{current_player} turn')
        coordinate = get_move()

        if model.is_valid_move(current_board, coordinate):
            current_board = model.make_move(current_board, coordinate, current_player)
            model.save_game(current_board, first_player, play_mode)

        else:
            print('Invalid move')
            continue

        view.render(current_board)

        winner = model.get_winner(current_board)

        if winner == 'x':
            print('X wins')
            break

        elif winner == 'o':
            print('O wins')
            break

        if model.is_full(current_board):
            print('Draw! No winners')
            break


def play_mode_2():
    """A method to control the play with the AI heuristic"""
    print('Wellcome in Tic-Tac-Toe AI Mode \n ')
    play_mode = 2

    loaded_game = model.load_game()
    current_board = loaded_game[0]
    first_player = loaded_game[1]

    if not modelai.terminal(current_board):
        view.render(current_board)

    else:
        current_board = model.new_board()
        view.render(current_board)

    while True:
        if modelai.terminal(current_board):
            if not model.get_winner(current_board):
                print('Draw! No winners')

            else:
                print(f'{model.get_winner(current_board)} wins')

            break

        if model.player(current_board, modelai.MIN_PLAYER) == modelai.MAX_PLAYER:  # AI's turn
            print(f'{modelai.MAX_PLAYER} turn')
            best_move = modelai.max_value(current_board)[1]
            current_board = model.make_move(current_board, best_move, modelai.MAX_PLAYER)
            view.render(current_board)
            model.save_game(current_board, modelai.MIN_PLAYER, play_mode)

        elif model.player(current_board, modelai.MIN_PLAYER) == modelai.MIN_PLAYER:  # User's turn
            print(f'{modelai.MIN_PLAYER} turn')
            adversary_move = get_move()
            if model.is_valid_move(current_board, adversary_move):
                current_board = model.make_move(current_board, adversary_move, modelai.MIN_PLAYER)
                model.save_game(current_board, modelai.MIN_PLAYER, play_mode)
            else:
                print('Invalid move')
                continue

            view.render(current_board)


def play():
    loaded_game = model.load_game()
    current_board = loaded_game[0]
    mode = loaded_game[2]

    if not modelai.terminal(current_board) and mode == 1:
        play_mode_1()
    elif not modelai.terminal(current_board) and mode == 2:
        play_mode_2()

    else:
        play_mode = input('Welcome to Tic-Tac-Toe\nPlease enter 1 for entering 2 players mode\n2 for AI Mode:')
        while True:
            if play_mode == '1':
                play_mode_1()
                break
            elif play_mode == '2':
                play_mode_2()
                break
            else:
                input('Invalid input!\nPlease enter 1 for entering 2 players mode\n2 for AI Mode:')


if __name__ == "__main__":
    play()

