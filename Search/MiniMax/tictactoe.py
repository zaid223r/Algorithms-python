import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    # 
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_possible_actions = []
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] != X and board[i][j] != O:
                all_possible_actions.append((i,j)) 
    return all_possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        if type(action) == tuple:
            i,j = action
            if board[i][j] != X and board[i][j] != O:
                new_board = [row[:] for row in board]
                new_board[i][j] = player(new_board)
                return new_board
            else :
                raise NotImplementedError
        else:
            raise NotImplementedError

    except NotImplementedError as s:
        return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        # check vertical
            for row in board:
                if row == [player] * 3:
                    return player

        # check horizontal
            for i in range(3):
                column = [board[x][i] for x in range(3)]
                if column == [player] * 3:
                    return player
        
        # check diagonal
            if [board[i][i] for i in range(0, 3)] == [player] * 3:
                return player

            elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
                return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    _win = winner(board)
    if _win == X:
        return 1
    elif _win == O:
        return -1
    else:
        if len(actions(board)) == 0:
            return 0
        else:
            return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # 
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move
    # 
    # _player = player(board)
    # if _player == X:
    #     print(f"maxvalue {max_value(board)} for {_player}")
    #     return max_value(board)
    # else:
    #     print(f"minvalue {max_value(board)} for {_player}")

    if terminal(board):
        return None
    elif player(board)==X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]