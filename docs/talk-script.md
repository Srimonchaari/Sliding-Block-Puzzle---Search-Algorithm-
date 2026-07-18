# Talk Script — 10 minutes, 13 slides

Say this in your own words — don't read it word for word. Each line is what to
SAY, not what's already written on the slide.

---

**Slide 1 — Title (30s)**
- "I'm presenting the Sliding Block Puzzle problem: solving the 8-puzzle with
  two different search algorithms."
- "One blind search, one guided search — both written from scratch, no
  algorithm libraries, as required."

**Slide 2 — Agenda (20s)**
- "I'll cover the problem, the theory behind both algorithms, then my
  measured results comparing them."

**Slide 3 — The Problem (40s)**
- "This is a 3x3 puzzle: 8 numbered tiles plus one blank space."
- "The blank can slide into whichever tile is next to it — up, down, left,
  or right."
- "The start and target boards were fixed by the assignment — I didn't
  choose them."
- "My program has to report three things for each algorithm: how many
  states it expanded, the most states it held in memory at once, and how
  many moves the solution took."

**Slide 4 — States, moves, search tree (50s)**
- "A 'state' is just one snapshot of the board."
- "'Expanding' a state means generating every board reachable in exactly
  one slide — up to 4 possibilities."
- "If you keep expanding states, you build a tree: the start board is the
  root, and solving the puzzle means finding a path down that tree to the
  target board."
- "g(n), h(n), f(n) are standard notation I'll use in a moment for A*."

**Slide 5 — BFS (70s)**
- "BFS is the uninformed algorithm — it doesn't know anything about which
  direction is 'closer' to the goal."
- "It uses a queue: first-in, first-out. It always expands whichever state
  has been waiting longest."
- "That means it checks every state 1 move away before any state 2 moves
  away — level by level, like ripples in a pond."
- "Because of that, the very first time it reaches the target, it's
  guaranteed to be the shortest possible solution."
- "The cost is memory — it has to hold every state at the current level at
  once."

**Slide 6 — A* (90s)**
- "A* is the informed search — it uses a heuristic to guess how far a state
  is from the goal, and always expands whichever state looks most
  promising."
- "The formula is f(n) = g(n) + h(n). g is the real cost so far — how many
  moves we've already made. h is an estimate of the moves still needed."
- "My heuristic is Manhattan distance: for every tile, I add up how many
  rows and columns it is away from where it belongs, ignoring the other
  tiles."
- "This heuristic is admissible — it never overestimates — because real
  moves can only cost the same or more, since tiles have to go around each
  other. That's what keeps A* guaranteed to still find the optimal
  solution."

**Slide 7 — Solvability (40s)**
- "Before running the search, it's worth knowing not every configuration is
  even solvable — exactly half aren't."
- "There's a simple check: count 'inversions' — pairs of tiles out of
  order. If that count is even, it's solvable."
- "I checked our start state — it's even, so a solution is guaranteed to
  exist, which matches both algorithms actually finding one."

**Slide 8 — Results table (50s)**
- "Here are my actual measured numbers, from running both algorithms on the
  exact same start and target."
- "Both found the same 28-move solution — so both are correct and optimal."
- "But BFS expanded 178,223 states; A* only needed 726 — about 245 times
  fewer."
- "Memory: BFS peaked at 185,046 states; A* only 1,444."
- "Time: BFS took about 1.5 seconds; A* took 8 milliseconds."

**Slide 9 — Bar chart / heatmap (30s)**
- "Visually, A* barely registers next to BFS on every single metric — same
  answer, drastically less work."

**Slide 10 — Why Manhattan distance (40s)**
- "I chose Manhattan distance over simpler options like counting misplaced
  tiles, because Manhattan distance expands far fewer nodes for barely any
  extra computation."
- "There are stronger heuristics, like Manhattan distance plus linear
  conflict, but they add real implementation complexity for a smaller
  extra gain — not needed for this puzzle size."

**Slide 11 — Context / benchmarks (30s)**
- "For context: the hardest possible 8-puzzle needs 31 moves, proven by
  full computer search. Our 28-move case is a genuinely hard instance."
- "My BFS-vs-A* gap also matches the same pattern reported in standard AI
  textbooks."

**Slide 12 — Observations / conclusions (40s)**
- "Three takeaways: both algorithms are correct and optimal — same answer."
- "The intelligence in A* comes entirely from the heuristic, not from the
  algorithm structure itself."
- "And the real bottleneck for BFS is memory, not just time — that's what
  would make it completely impractical on a bigger puzzle, like the
  15-puzzle."

**Slide 13 — References (10s)**
- "These are my sources for the theory and the benchmark numbers I
  referenced."

**Closing**
- "That's my comparison of BFS and A* on the sliding block puzzle. Happy to
  answer questions."

---

## Timing check
Total ≈ 9.5–10 minutes at a normal speaking pace. If running long, cut
detail from Slide 6 (A*) or Slide 11 (benchmarks) first — Slides 3, 5, 6,
and 8 are the ones a grader is most likely to probe on, so keep those solid.

## Likely questions from the tutor — be ready for these
- "Why is Manhattan distance admissible?" → tiles can only need MORE moves
  than a straight-line count, never fewer, because they must go around
  each other.
- "Why does BFS guarantee the shortest path?" → it finishes an entire
  depth level before starting the next, so no shorter path could have
  been skipped.
- "What would happen with a bad heuristic (e.g. h(n)=0)?" → A* becomes
  identical to BFS (this follows directly from f(n) = g(n) + h(n)).
- "How do you avoid infinite loops / re-visiting states?" → the visited
  set (BFS) / best-known-cost map (A*) — explained on the pseudocode
  slides.
- "Why not use Python's built-in queue/heapq?" → allowed under the rules
  (they're data structures, not search algorithms) but we wrote our own
  anyway for full transparency and to keep the code minimal/dependency-free.
