def bfs(start, goal, next_states):
    Frontier = {start}
    Visited = set()
    Parent = {start: start}
    while len(Frontier) > 0:
        NewFrontier = set()
        for s in Frontier:
            for ns in next_states(s):
                if ns not in Visited and ns not in Frontier:
                    NewFrontier.add(ns)
                    Parent[ns] = s
                    if ns == goal:
                        return path_to(goal, Parent)
                        
def path_to(state, Parent):
    p = Parent[state]
    if p == state:
        return [state]
    return path_to(p, Parent) + [state]