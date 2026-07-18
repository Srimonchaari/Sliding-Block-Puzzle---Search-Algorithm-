# Breadth-First Search (uninformed search) for the sliding block puzzle.

from puzzle import get_moves, to_tuple


def bfs(start, target):
    target_key = to_tuple(target)
    start_key = to_tuple(start)

    # Each queue entry is (board, path_so_far).
    # path_so_far is the list of boards from start up to this board.
    queue = [(start, [start])]
    visited = {start_key}

    node_expansions = 0
    max_nodes_in_memory = 1  # 1 state (the start) is in memory right now

    while len(queue) > 0:
        board, path = queue.pop(0)  # take from the FRONT (FIFO)

        if to_tuple(board) == target_key:
            return path, node_expansions, max_nodes_in_memory

        node_expansions += 1

        for child in get_moves(board):
            child_key = to_tuple(child)
            if child_key not in visited:
                visited.add(child_key)
                queue.append((child, path + [child]))

        # after adding this round's children, check if memory usage grew
        nodes_in_memory = len(queue) + len(visited)
        if nodes_in_memory > max_nodes_in_memory:
            max_nodes_in_memory = nodes_in_memory

    return None, node_expansions, max_nodes_in_memory  # no solution found
