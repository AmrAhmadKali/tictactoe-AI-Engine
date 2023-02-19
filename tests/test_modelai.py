import modelai

empty_board = [[None, None, None], [None, None, None], [None, None, None]]
full_board = [['x', 'o', 'o'], ['o', 'x', 'x'], ['x', 'o', 'o']]


def test_actions():
    global empty_board
    global full_board

    assert len(modelai.actions(empty_board)) == 9
    assert not modelai.actions(full_board)
    assert modelai.actions([[None, 'x', 'o'], [None, 'o', 'x'], ['x', None, None]]) == {(0, 0), (1, 0), (2, 1), (2, 2)}


def test_terminal():
    global empty_board
    global full_board

    assert not modelai.terminal(empty_board)
    assert modelai.terminal(full_board)
    assert not modelai.terminal([[None, 'x', 'o'], [None, 'o', 'x'], ['x', None, None]])


def test_utility():
    board_for_max_player = [['x', 'o', None], ['o', 'x', 'x'], ['o', None, 'x']]
    board_for_min_player = [[None, 'x', 'o'], [None, 'o', 'x'], ['o', None, None]]
    global full_board

    assert modelai.utility(board_for_min_player) == -1
    assert modelai.utility(full_board) == 0
    assert modelai.utility(board_for_max_player) == 1


def test_max_value():
    assert modelai.max_value([['x', None, 'o'], [None, 'o', None], ['x', None, 'o']]) == (1, (1, 0))
    assert modelai.max_value([['x', 'o', None], ['o', 'o', 'x'], ['x', None, None]]) == (0, (2, 1))


def test_min_value():
    assert modelai.min_value([['x', None, 'o'], [None, None, None], ['x', None, 'o']]) == (-1,)
    assert modelai.min_value([['x', 'o', None], ['o', 'o', 'x'], ['x', 'x', None]]) == (0,)
