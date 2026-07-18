# A* Search (informed search) for the sliding block puzzle.
# Uses the Manhattan distance heuristic: f(n) = g(n) + h(n)

from puzzle import get_moves, to_tuple, goal_positions, manhattan_distance


def pop_best(frontier):
    # Find and remove the entry with the smallest f_score.
    # frontier is a list of [f_score, board, path, g_score].
    best_index = 0
    for i in range(1, len(frontier)):
        if frontier[i][0] < frontier[best_index][0]:
            best_index = i
    return frontier.pop(best_index)


def a_star(start, target):
    target_key = to_tuple(target)
    positions = goal_positions(target)

    start_h = manhattan_distance(start, positions)
    # Each frontier entry: [f_score, board, path_so_far, g_score]
    frontier = [[start_h, start, [start], 0]]
    best_g_score = {to_tuple(start): 0}

    node_expansions = 0
    max_nodes_in_memory = 1

    while len(frontier) > 0:
        f_score, board, path, g_score = pop_best(frontier)
        board_key = to_tuple(board)

        if board_key == target_key:
            return path, node_expansions, max_nodes_in_memory

        # This entry may be an outdated, worse copy of a state we
        # already reached more cheaply later on -- skip it.
        if g_score > best_g_score.get(board_key, g_score):
            continue

        node_expansions += 1

        for child in get_moves(board):
            child_key = to_tuple(child)
            new_g_score = g_score + 1  # every move costs 1

            if new_g_score < best_g_score.get(child_key, float("inf")):
                best_g_score[child_key] = new_g_score
                new_f_score = new_g_score + manhattan_distance(child, positions)
                frontier.append([new_f_score, child, path + [child], new_g_score])

        nodes_in_memory = len(frontier) + len(best_g_score)
        if nodes_in_memory > max_nodes_in_memory:
            max_nodes_in_memory = nodes_in_memory

    return None, node_expansions, max_nodes_in_memory  # no solution found
