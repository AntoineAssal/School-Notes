def dfs(start, goal, next_states):
    Stack = [start]
    Parent = {start: start}
    while len(Stack) > 0:
        state = Stack.pop()
        for ns in next_states(state):
            if ns not in Parent:
                Parent[ns] = state
                Stack.append(ns)
            if ns == goal:
                return path_to(start, goal, Parent)


def path_to(start, state, Parent):
    Path = [state]
    while state != start:
        state = Parent[state]
        Path = [state] + Path
        return Path
