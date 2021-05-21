def depth_limited_search(state, goal, next_states, Path, PathSet, limit):
    if state == goal:
        return Path
    if len(Path) == limit:
        return None
    for ns in next_states(state):
        if ns not in PathSet:
            Path   .append(ns)
            PathSet.add(ns)
            Result = depth_limited_search(ns, goal, next_states, Path, PathSet, limit)
            if Result != None:
                return Result
            Path   .pop()
            PathSet.remove(ns)
    return None