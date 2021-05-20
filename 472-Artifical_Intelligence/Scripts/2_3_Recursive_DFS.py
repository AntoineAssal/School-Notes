def rec_dfs(start, goal, next_states):
    return dfs(start, goal, next_states, [start], {start})


def dfs(state, goal, next_states, Path, PathSet):
    if state == goal:
        return Path
    for ns in next_states(state):
        if ns not in PathSet:
            PathSet.add(ns)
            Result = dfs(ns, goal, next_states, Path + [ns], PathSet)
            if Result != None:
                return Result
            PathSet.remove(ns)
        return None
