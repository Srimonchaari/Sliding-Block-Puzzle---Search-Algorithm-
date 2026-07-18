![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![No Libraries](https://img.shields.io/badge/Search%20Algorithms-Hand--written-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-Coursework-lightgrey)

# Sliding Block Puzzle: BFS vs A*

This is our seminar project for Cognitive Systems 2: Behavior Control. We solve the classic 8 puzzle (a 3x3 sliding block puzzle) using two different search algorithms, and we compare how each one performs.

This README is written so that anyone in the group can open it and understand the whole project, even if you have never written code before. Read it top to bottom the first time. After that, use the table of contents to jump to whatever section you need.

## Table of contents

1. [What is this project](#1-what-is-this-project)
2. [The task sheet, explained](#2-the-task-sheet-explained)
3. [The problem, in plain words](#3-the-problem-in-plain-words)
4. [The idea behind the solution](#4-the-idea-behind-the-solution)
5. [How the project is organised](#5-how-the-project-is-organised)
6. [Architecture diagram](#6-architecture-diagram)
7. [What each file does](#7-what-each-file-does)
8. [How to run it yourself](#8-how-to-run-it-yourself)
9. [Our results](#9-our-results)
10. [Rules we had to follow, and how we followed them](#10-rules-we-had-to-follow-and-how-we-followed-them)
11. [The presentation slides](#11-the-presentation-slides)
12. [Common questions](#12-common-questions)
13. [Credits and sources](#13-credits-and-sources)

## 1. What is this project

Our lecturer gave us a task sheet (`SEMINAR TASK.pdf` in this folder) asking us to write a program that solves a sliding block puzzle using two different search methods, then present our findings.

We built:

- A working Python program that solves the puzzle two different ways
- A set of measurements comparing how each method performs
- A slide deck explaining the theory and our results

Everything is written from scratch. We do not import any ready made search algorithm from a library. That was a strict rule on the task sheet, and we followed it on purpose so that the whole group understands every step the program takes.

## 2. The task sheet, explained

Here is the task broken into plain questions and answers, so nobody has to go dig through the PDF to remember what we were asked to do.

**Q: What puzzle are we solving?**
A: A 3x3 sliding block puzzle, also called the 8 puzzle. It has 8 numbered tiles and one empty space. You slide tiles into the empty space to reorder them.

**Q: What exact starting layout and target layout did we get?**
A: These were fixed by the task sheet, we did not get to choose them.

Start:
```
8 7 6
5 4 3
2 1 _
```

Target:
```
_ 1 2
3 4 5
6 7 8
```

The underscore is the empty space. Note that even the position of the empty space in the target matters, it has to end up in the top left corner.

**Q: How many search algorithms do we need?**
A: At least two.

- One uninformed algorithm, meaning it has no sense of direction toward the goal. Options were breadth first search or depth first search.
- One informed algorithm, specifically A* search, which must use a heuristic that never overestimates the true cost (this is called an admissible heuristic).

**Q: What do we need to measure and show for each algorithm?**
A: Three things, for both algorithms:

1. The number of node expansions (how many board states the algorithm actually processed)
2. The maximum number of nodes held in memory at any point
3. The number of moves in the final solution

**Q: Are we allowed to use any programming language?**
A: Yes, the language is free to choose. We picked Python because it is the easiest language to read and teach to people with no coding background.

**Q: Are we allowed to use libraries?**
A: Not for the search algorithms themselves. We are not allowed to import a ready made breadth first search, depth first search, or A* implementation from any library. We had to write the algorithm logic ourselves. Using basic language features (like Python lists, tuples, and dictionaries) is fine, since those are not search algorithms.

**Q: What do we need to prepare besides the code?**
A: A 10 minute presentation covering the theory behind the algorithms we used, and a discussion of our results.

**Q: How is this graded?**
A: Out of 10 points total. 4 points for the program, 6 points for the presentation and discussion. These points get added to our exam score.

## 3. The problem, in plain words

Picture a small tray with 9 slots arranged in a 3x3 grid. Eight of the slots have numbered tiles in them, and one slot is empty. You can only move a tile that sits right next to the empty slot, sliding it into that empty space. That one move also moves the empty space to where the tile used to be.

Our goal is to go from a scrambled starting layout to a neatly ordered target layout, using as few slides as possible, and using a computer program to figure out the exact sequence of slides needed.

The tricky part is that the number of possible layouts is huge (362,880 different arrangements of 9 tiles), so the program cannot just try random moves. It needs a proper strategy for exploring possible moves without wasting time, and that strategy is called a search algorithm.

## 4. The idea behind the solution

Think of every possible board layout as a single point, and every legal slide as a line connecting two points. If you connect every possible layout to every other layout this way, you get a giant web of connected points. Our starting layout is one point in that web, and our target layout is another point somewhere else in it.

Solving the puzzle means finding a path through that web from the start point to the target point. A search algorithm is simply a strategy for exploring that web efficiently instead of wandering randomly.

We used two different strategies, on purpose, so we could compare them:

**Strategy one: Breadth First Search (BFS)**
This strategy explores every layout that is one slide away from the start, then every layout that is two slides away, then three, and so on. It never skips ahead. Because of this, the very first time it reaches the target, it is guaranteed to have found the shortest possible solution. The downside is that it has to remember a huge number of layouts at once, which uses a lot of memory and takes a long time.

**Strategy two: A* Search**
This strategy is smarter. At every step, it uses a quick estimate (called a heuristic) of how close a layout is to the target, and always tries the most promising looking layout next. Our heuristic is called Manhattan distance, and for each tile it simply adds up how many rows and columns that tile is away from where it belongs. This estimate never overguesses, so A* is still guaranteed to find the shortest solution, but it usually gets there by checking far fewer layouts than BFS.

Both strategies are correct. The whole point of our project is to show, with real numbers, how much more efficient the smarter strategy is.

## 5. How the project is organised

We kept the code split into small, focused files. Each file does one clear job, and none of them are long or complicated.

```
Sliding-Block-Puzzle/
├── README.md              This file
├── SEMINAR TASK.pdf        The original task sheet from our lecturer
├── puzzle.py               The board itself: how it looks, how tiles move
├── bfs.py                  The uninformed search algorithm
├── astar.py                The informed search algorithm and its heuristic
├── main.py                 Runs both algorithms and prints the comparison
└── docs/
    ├── index.html                             Our presentation slides (open in a browser, works on mobile too)
    ├── Sliding-Block-Puzzle-BFS-vs-Astar.pptx   The same slides as a PowerPoint file, for sharing
    └── talk-script.md                          What to actually say for each slide, timed to 10 minutes
```

## 6. Architecture diagram

This shows how the pieces of the program depend on each other. `main.py` is the entry point, the file you actually run. It pulls in the puzzle logic and both search algorithms, runs them, and prints the results.

```
                              +--------------------+
                              |      main.py       |
                              |   (entry point)    |
                              +--------------------+
                                         |
                       runs both algorithms, prints results
                                         |
                +------------------------+----+
                |                             |
    +----------------------+      +----------------------+
    |        bfs.py        |      |       astar.py       |
    | Breadth First Search |      |A* Search + heuristic |
    +----------------------+      +----------------------+
                |                             |
                +------------------------+----+
                                         |
                                   both rely on
                                         |
                          +----------------------------+
                          |         puzzle.py          |
                          | board layout, legal moves, |
                          |     Manhattan distance     |
                          +----------------------------+
```

In plain words: `puzzle.py` is the shared foundation both algorithms stand on. It knows what the board looks like and how tiles are allowed to move, but it does not know anything about searching. `bfs.py` and `astar.py` each take that foundation and add their own strategy on top of it. `main.py` ties everything together and is the only file you actually need to run.

## 7. What each file does

**`puzzle.py`**
This file has no search logic at all. It only describes the puzzle itself.

- `START` and `TARGET`, the two fixed layouts from the task sheet
- `find_blank(board)`, finds where the empty space currently is
- `copy_board(board)`, makes a safe copy of a layout so we never accidentally change the original
- `to_tuple(board)`, converts a layout into a format that can be stored in a set or dictionary (needed so we can remember which layouts we already looked at)
- `goal_positions(target)`, works out where every tile belongs in the target layout
- `manhattan_distance(board, positions)`, our heuristic, explained in section 4
- `print_board(board)`, prints a layout so a human can read it
- `get_moves(board)`, generates every layout reachable in exactly one slide

**`bfs.py`**
Contains one function, `bfs(start, target)`. It explores layouts level by level using a first in first out queue, and counts how many layouts it expanded and the largest number of layouts it ever held at once.

**`astar.py`**
Contains one function, `a_star(start, target)`. It explores layouts using a priority list ranked by the heuristic, always trying the most promising layout next, and keeps the same two counts as BFS.

**`main.py`**
This is the file you run. It calls both `bfs` and `a_star` on the same start and target, times each one, prints the solution path, and finally prints a side by side comparison table.

## 8. How to run it yourself

You need Python installed on your computer (version 3.10 or newer is safest, but most versions work). No extra installation is needed, there is nothing to download beyond Python itself.

1. Open a terminal (on Mac, search for Terminal in Spotlight)
2. Move into the project folder, for example:
   ```
   cd path/to/Sliding-Block-Puzzle
   ```
3. Run the program:
   ```
   python3 main.py
   ```
4. Read the output. It will show the start and target boards, the move count, the node expansions, the memory used, the time taken, and a comparison table at the end.

If you want to look at just one algorithm on its own, you can also open `puzzle.py`, `bfs.py`, or `astar.py` in a text editor to read the code directly. Every important line has a short comment explaining what it does.

## 9. Our results

We ran both algorithms on the exact start and target layout from the task sheet. Both found a solution using 28 moves, which confirms both are correct. The difference is in how much work each one had to do to get there.

| Metric | BFS (uninformed) | A* (informed) | Difference |
|---|---|---|---|
| Moves in solution | 28 | 28 | identical, both optimal |
| Node expansions | 178,223 | 726 | about 245 times fewer |
| Max nodes in memory | 185,046 | 1,444 | about 128 times fewer |
| Time to solve | 1.55 seconds | 0.008 seconds | about 190 times faster |

**What this tells us:** both algorithms are correct, and both give the shortest possible solution. The A* algorithm gets to that same answer while doing dramatically less work, because its heuristic gives it a sense of direction that BFS simply does not have. BFS has to blindly check almost every nearby layout, while A* can tell which layouts are worth checking and skip the rest.

## 10. Rules we had to follow, and how we followed them

| Rule from the task sheet | How we followed it |
|---|---|
| Use at least two different search algorithms | We wrote BFS (uninformed) and A* (informed) |
| A* must use an admissible heuristic | We use Manhattan distance, which never overestimates the true remaining cost |
| No libraries containing search algorithm implementations | Every part of BFS and A*, including the queue and the priority list, is written by us in plain Python, no imports for the algorithms themselves |
| Must count node expansions | Both algorithms return this number |
| Must count max nodes held in memory | Both algorithms track and return this number |
| Must count moves needed to solve | Calculated directly from the returned solution path |
| Start and target layouts, including blank position, must match exactly | Hardcoded in `puzzle.py` exactly as given on the task sheet |
| Prepare a presentation on theory and results | See `docs/index.html` and `docs/talk-script.md` |

## 11. The presentation slides

Open `docs/index.html` in any web browser (just double click the file, or drag it into a browser window) to see our full slide deck. It covers the problem, the theory behind both algorithms, our measured results, and our conclusions. It also works fine on a phone, so anyone in the group can review it on the go.

We also have `docs/Sliding-Block-Puzzle-BFS-vs-Astar.pptx`, a PowerPoint file with the same slides, so it can be shared, edited, or presented from without needing a browser.

`docs/talk-script.md` has the actual words to say for each slide, timed to fit a 10 minute talk, along with a list of questions the tutor is likely to ask and how to answer them.

## 12. Common questions

**Q: I have never coded before, can I still understand this project?**
A: Yes. Read sections 1 through 4 of this README first, they explain everything in plain language with no code. Sections 5 through 8 are only needed if you want to actually open and read the code files.

**Q: What is a node expansion, in simple terms?**
A: Every time the program picks a board layout and checks all the ways it could slide a tile from there, that counts as one expansion. Fewer expansions means less wasted effort.

**Q: Why do both algorithms find the same 28 move answer?**
A: Because both are designed to guarantee the shortest possible solution. BFS does this by checking every shorter option first. A* does this because its heuristic never overguesses, so it can never accidentally skip past the true shortest path.

**Q: If A* is so much better, why bother with BFS at all?**
A: The task sheet asked for both, on purpose, so we could see the difference for ourselves. BFS is also simpler to understand and does not need a heuristic, which makes it a useful baseline before introducing something smarter like A*.

**Q: Where do the numbers in section 9 come from?**
A: They come directly from running `main.py` on this exact computer, using the exact start and target layout from the task sheet. Anyone can reproduce them by running the program themselves.

## 13. Credits and sources

The theory slides reference a few outside sources for background facts, listed here and also on the references slide in `docs/index.html`.

- Reinefeld, A., *Complete Solution of the Eight Puzzle and the Benefit of Node Ordering in IDA-star*, IJCAI 1993
- Russell, S. and Norvig, P., *Artificial Intelligence: A Modern Approach*
- NIT Rourkela, *Analysis and Implementation of Admissible Heuristics in 8 Puzzle Problem*
- UML course project, *Analyzing the A* Search Heuristics with the Solutions of the 8 Puzzle*
- Princeton COS226, 8 Puzzle assignment
- MIT 6.1200J, *Mathematics for Computer Science*, lecture notes
