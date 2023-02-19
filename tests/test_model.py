import model
from os.path import exists

empty_board = [[None, None, None], [None, None, None], [None, None, None]]
full_board = [['x', 'o', 'o'], ['o', 'x', 'x'], ['x', 'o', 'o']]


def test_new_board():
    # Arrange
    global empty_board
    # Act
    new_board = model.new_board()
    # Assert
    assert new_board == empty_board


def test_is_valid_move():
    global empty_board

    assert model.is_valid_move(empty_board, (0, 0))
    assert not model.is_valid_move([['o', None, None], [None, None, None], [None, None, None]], (0, 0))


def test_player():
    global empty_board

    assert model.player(empty_board, 'x') == 'x'
    assert model.player(empty_board, 'o') == 'o'
    assert model.player([['o', 'x', None], [None, None, None], [None, None, None]], 'o') == 'o'
    assert model.player([['o', 'x', None], [None, None, None], [None, None, None]], 'x') == 'x'


def test_make_move():
    global empty_board

    assert model.make_move(empty_board, (0, 0), 'x') == [['x', None, None], [None, None, None], [None, None, None]]
    assert model.make_move([['x', None, None], [None, None, None], [None, None, None]], (2, 2), 'o') == \
           [['x', None, None], [None, None, None], [None, None, 'o']]


def test_save_game():
    # Arrange
    board = [['x', None, None], [None, None, None], [None, None, 'o']]
    expected_board = '[["x", null, null], [null, null, null], [null, null, "o"]]'
    expected_player = '"x"'
    expected_mode = '1'
    # Act
    model.save_game(board, 'x', 1)
    with open('data\\board.json') as board_file:
        board_content = board_file.read()
    with open('data\\player.json') as player_file:
        player_content = player_file.read()
    with open('data\\mode.json') as mode_file:
        mode_content = mode_file.read()

    # Assert
    assert exists('data\\board.json') and exists('data\\player.json') and exists('data\\mode.json')
    assert board_content == expected_board and player_content == expected_player and mode_content == expected_mode


def test_load_game():
    # Arrange
    board = [['x', None, None], [None, None, None], [None, None, 'o']]
    player = 'x'
    mode = 1
    # Act
    model.save_game(board, player, mode)
    loaded_game = model.load_game()
    # Assert
    assert loaded_game == (board, player, mode)


def test_get_winner():
    global empty_board
    global full_board

    assert not model.get_winner(empty_board)
    assert model.get_winner([['o', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]) == 'x'
    assert not model.get_winner(full_board)


def test_is_full():
    global empty_board
    global full_board

    assert not model.is_full(empty_board)
    assert model.is_full(full_board)