def search(start, goal, next_states):
    limit = 1
    while True:
        Path = dls(start, goal, next_states, [start], {start}, limit)
        if Path != None:
            return Path
        limit += 1


def dls(state, goal, next_states, Path, PathSet, limit):
    if state == goal:
        return Path
    if len(Path) == limit:
        return None
    for ns in next_states(state):
        if ns not in PathSet:
            Path.append(ns)
            PathSet.add(ns)
            Result = dls(ns, goal, next_states, Path, PathSet, limit)
            if Result != None:
                return Result
            else:
                Path.pop()
                PathSet.remove(ns)
    return None
