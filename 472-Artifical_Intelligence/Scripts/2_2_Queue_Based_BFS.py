from collections import deque


def bfs_queue(start, goal, next_states):
    Frontier = deque([start])
    Parent = {start: start}
    while len(Frontier) > 0:
        state = Frontier.popleft()
        if state == goal:
            return path_to(state, Parent)
        new_states = next_states(state)
        for ns in new_states:
            if ns not in Parent:
                Parent[ns] = state
                Frontier.append(ns)


def path_to(state, Parent):
    p = Parent[state]
    if p == state:
        return [state]
    return path_to(p, Parent) + [state]
