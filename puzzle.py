# Sliding Block Puzzle (8-puzzle) solver
# Board is represented as a list of 3 rows, each row a list of 3 numbers.
# 0 represents the blank tile.

START = [
    [8, 7, 6],
    [5, 4, 3],
    [2, 1, 0]
]

TARGET = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]


def find_blank(board):
    # Scan every cell until we find the 0 (blank), return its (row, col).
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return (row, col)


def copy_board(board):
    # Make a brand new list-of-lists with the same numbers.
    # We need this so moving a tile never changes the original board.
    new_board = []
    for row in board:
        new_board.append(list(row))
    return new_board


def to_tuple(board):
    # Convert list-of-lists (editable) into tuple-of-tuples (frozen),
    # so it can be stored in a set/dict as a "seen this state before" marker.
    return tuple(tuple(row) for row in board)


def goal_positions(target):
    # Build a lookup: tile number -> (row, col) it belongs at in the target.
    positions = {}
    for row in range(3):
        for col in range(3):
            tile = target[row][col]
            positions[tile] = (row, col)
    return positions


def manhattan_distance(board, positions):
    # Sum of |row difference| + |col difference| for every non-blank tile.
    total = 0
    for row in range(3):
        for col in range(3):
            tile = board[row][col]
            if tile != 0:
                goal_row, goal_col = positions[tile]
                total += abs(row - goal_row) + abs(col - goal_col)
    return total


def print_board(board):
    for row in board:
        line = " ".join(str(tile) if tile != 0 else "_" for tile in row)
        print(line)


def get_moves(board):
    # Returns a list of all boards reachable in exactly one move.
    row, col = find_blank(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    children = []

    for d_row, d_col in directions:
        new_row = row + d_row
        new_col = col + d_col

        if 0 <= new_row <= 2 and 0 <= new_col <= 2:
            child = copy_board(board)
            # swap blank with the tile at (new_row, new_col)
            child[row][col] = child[new_row][new_col]
            child[new_row][new_col] = 0
            children.append(child)

    return children
