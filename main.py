# Sliding Block Puzzle Solver -- entry point.
# Runs BFS (uninformed) and A* (informed) on the same start/target
# and prints the solution path plus the required comparison metrics.

import time
from puzzle import START, TARGET, print_board
from bfs import bfs
from astar import a_star


def print_path(path):
    # Printing every move for a ~28-move solution is too long for a live
    # demo, so we show only the start and the target boards.
    last_index = len(path) - 1
    for i, board in enumerate(path):
        if i == 0 or i == last_index:
            print(f"Move {i}:")
            print_board(board)
            print()
        elif i == 1:
            print(f"... {last_index - 1} moves omitted ...")
            print()


def run(name, search_function):
    start_time = time.time()
    path, expansions, max_nodes = search_function(START, TARGET)
    elapsed = time.time() - start_time

    moves = len(path) - 1
    print(f"--- {name} ---")
    print_path(path)
    print(f"Moves needed: {moves}")
    print(f"Node expansions: {expansions}")
    print(f"Max nodes in memory: {max_nodes}")
    print(f"Time taken: {elapsed:.4f} seconds")
    print()

    return moves, expansions, max_nodes, elapsed


if __name__ == "__main__":
    bfs_result = run("Breadth-First Search", bfs)
    astar_result = run("A* Search", a_star)

    print("--- Comparison ---")
    print(f"{'Metric':<22}{'BFS':>15}{'A*':>15}")
    labels = ["Moves", "Node expansions", "Max nodes in memory", "Time (s)"]
    for label, bfs_value, astar_value in zip(labels, bfs_result, astar_result):
        if label == "Time (s)":
            print(f"{label:<22}{bfs_value:>15.4f}{astar_value:>15.4f}")
        else:
            print(f"{label:<22}{bfs_value:>15}{astar_value:>15}")
