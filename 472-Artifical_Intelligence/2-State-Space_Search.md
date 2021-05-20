# State-Space Search


## Example: 8-Puzzle
- Suppose that we have `3X3` board. With any arrangement of `8` numbered tiles with an empty tile.
- Our `initial state` is the scrambled board on the left.
- `Goal state` is the sorted board with the numbers put in order and the empty tile on the bottom right corner or in the middle.
<p align="center">
<img src="https://i.imgur.com/pv5I40X.png" width="450"/>
</p>

- Most `AI` problems can be expressed in terms of going from an `initial state` to a `goal state`.
- There is no direct way to find a solution, so usually we list the possibilities and search through them.
  - **Brute Force Search** : Generates all possibilities and searches through them.
    - Obviously inefficient.
  - **Heuristic search** : Only try the possibilities based on the current best guess that they might lead to a good solution.

# What is State-Space
## 1. Initial State
- The starting state of the problem.
  - Unsolved puzzle.
  - Being at home.
## 2. Set of Operators
- Actions responsible for transition between states.
## 3. Goal Test Functions
- Applied to a state to determine if it is a `goal state`.
  - Solved puzzle.
  - Being at Concordia.
## 4. Path cost function
- Assigns a cost to a path so we can tell if it's preferable to another.

Now if we take the same example and make sense of what we just said.

<p align="center">
<img src="https://i.imgur.com/pv5I40X.png" width="450"/>
</p>

We already know what the `initial` and `goal` states should look like.
- Set of Operators : Blank square can move up, move down, move left, move right.
  - Or a numbered square can move up, down, left, right to replace a blank one.
- Goal test function : Current state should match the goal state.
- Path cost function : Each movement costs `1` movement.

## State-Space Graph Representation
- Each state is represented by a distinct node.
  - **A node is a state** not a tile in the puzzle.
- An edge/arc connects a node `s` to a node `s'` if `s'  ∈ SUCCESSOR(s)`.
- The state graph may contain more than one connected component.
- We can have cycles in the graph.
  - Cycles can prevent termination.
    - Blind search without a cycle checker might never terminate.

<p align="center">
<img src="https://i.imgur.com/DfDxCUD.png" width="450"/>
</p>

## State-Space Tree Representation
- Sometimes its better to use a tree representation with cycle checking.

<p align="center">
<img src="https://i.imgur.com/3ly98d6.png" width="450"/>
<img src="https://i.imgur.com/wWi1XNd.png" width="450"/>
</p>

