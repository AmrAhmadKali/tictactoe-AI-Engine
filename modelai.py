import model as model

MIN_PLAYER = 'o'
MAX_PLAYER = 'x'


def actions(s):
    """A method that, given a state s, return all the legal moves in this
    state (what spots are free on the board).
    """
    all_actions = set()
    for row in range(model.DIMENSION):
        for column in range(model.DIMENSION):
            if s[row][column] is None:
                possible_move = (row, column)
                all_actions.add(possible_move)
    if all_actions == set():
        print('Full board')
        return False
    return all_actions


def terminal(s):
    """A method that return True if the game is over (terminated), False if not"""
    winner = model.get_winner(s)

    if winner == 'x' or winner == 'o' or model.is_full(s):
        return True
    return False


def utility(s):
    """A method to mark the end of game with a specific number (utility): 1
    if Max_Player wins, 0 if draw and -1 if Min_player wins
    """
    if model.get_winner(s) == MAX_PLAYER:
        return 1
    elif model.get_winner(s) == MIN_PLAYER:
        return -1
    elif model.is_full(s):
        return 0


# @profile
def max_value(s):
    """A method to determine a move that maximize the Score for the
    MAX_PLAYER
    """
    if terminal(s):
        return utility(s),

    v = -3  # -3 is not a possible utility, but it is here like negative infinity for the specific case
    action_score = dict()
    for action in actions(s):
        v = max(v, min_value(model.make_move(s, action, MAX_PLAYER))[0])
        action_score.update({action: v})
    best_action = max(action_score, key=lambda k: action_score[k])
    return v, best_action


def min_value(s):
    """A method to calculate the minimum possible utility for the
    MIN_PLAYER at a given state of board
    """
    if terminal(s):
        return utility(s),

    v = 3  # 3 is not a possible utility, but it is here like positive infinity for the specific case
    for action in actions(s):
        v = min(v, max_value(model.make_move(s, action, MIN_PLAYER))[0])
    return v,
