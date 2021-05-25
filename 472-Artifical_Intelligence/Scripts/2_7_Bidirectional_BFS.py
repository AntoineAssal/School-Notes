def bi_BFS(start, goal, next_states):
    FrontierA = {start}
    ParentA = {start: start}
    FrontierB = {goal}
    ParentB = {goal: goal}
    while len(FrontierA) > 0 and len(FrontierB) > 0:
        NewFrontier = set()
        for s in FrontierA:
            for ns in next_states(s):
                if ns not in ParentA:
                    NewFrontier |= {ns}
                    ParentA[ns] = s
                    if ns in ParentB:
                        return combinePaths(ns, ParentA, ParentB)
        FrontierA = NewFrontier
        NewFrontier = set()
        for s in FrontierB:
            for ns in next_states(s):
                if ns not in ParentB:
                    NewFrontier |= {ns}
                    ParentB[ns] = s
                    if ns in ParentA:
                        return combinePaths(ns, ParentA, ParentB)
        FrontierB = NewFrontier


def path_to(state, Parent):
    p = Parent[state]
    if p == state:
        return [state]
    return path_to(p, Parent) + [state]


def combinePaths(state, ParentA, ParentB):
    Path1 = path_to(state, ParentA)
    Path2 = path_to(state, ParentB)
    return Path1[:-1] + Path2[::-1]
