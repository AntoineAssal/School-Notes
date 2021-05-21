# Lab 2 - State Space Search

## Question 1
Once upon a time a farmer went to the market and purchased a fox, a goose, and a bag of beans. On his way home, the farmer came to the bank of a river and rented a boat. But in crossing the river by boat, the farmer could carry only himself and a single one of his purchases - the fox, the goose, or the bag of the beans.

If left alone, the fox would eat the goose, and the goose would eat the beans. The farmer’s challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.

Represent this problem as a search problem. Choose a representation for the
problem’s states and:

1. Write down the initial state.
2. Write down the goal state.
3. Write down all illegal states.
4. Write down the possible actions.
5. Draw the state space for this problem.
6. Find a series of moves to solve this problem.

### Solution   
#### Initial State
We can represent it as `position(farmer, fox, goose, beans)` and our initial state would be `positional(s, s, s, s)`

#### Goal State
`position(g, g, g, g)`
#### Illegal States
Given the conditions we need to respect, some problems arise in different scenarios, making some of the possible states illegal.
- Farmer reaches goal alone or the opposite:

`position(g, s, s, s)`

`position(s, g, g, g)`
- Fox left alone with goose:

`position(g, s, s, g)`

`position(s, g, g, s)`

- Goose left alone with beans:

`position(g, g, s, s)`

`position(s, s, g, g)`

#### Possible Actions
`moveToGoal(farmer, null)`

`moveToGoal(farmer, fox)`

`moveToGoal(farmer, goose)`

`moveToGoal(farmer, beans)`

`moveToStart(farmer, null)`

`moveToStart(farmer, fox)`

`moveToStart(farmer, goose)`

`moveToStart(farmer, beans)`

#### State Space Graphic Representation
#### Possible Solution


<hr>

## Question 2

Assume that `S` is the initial state and `G`<sub>`1`</sub> and `G`<sub>`2`</sub> are the goal states. The possible actions between states are indicated by arrows. The number labelling each arc is the cost of the action. For example the cost of going from state `S` to `A` is `3`. The number in bold italic near each state is the valuee of the *heuristic function* `h` at that state. For example, the value of `h` at state `C` is `3`. When all else is equal, expand states in alphabetical order.

<img src="https://i.imgur.com/g1DQOPk.png">

Show the states visited, along with open and closed lists at each step for each of the following search strategy.

1. Breadth-First Search
2. Depth-First Search
3. Iterative Deepening Depth-First Search
4. Uniform Cost Search
5. Hill Climbing
6. Best-Fit Search
7. Algorithm A*
