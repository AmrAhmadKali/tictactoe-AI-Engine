"""This module serves as View Element in an MVC Architecture"""
import model


def render(board):
    print('\t  |0  1  2')
    print('\t  __________')
    for row in range(model.DIMENSION):
        print('\t', row, end='|')
        for column in range(model.DIMENSION):
            if board[row][column] is not None:
                print(board[row][column], end='  ')
            else:
                print('-', end='  ')
        print('|')
    print('\t  __________')
